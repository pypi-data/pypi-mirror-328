# SPDX-FileCopyrightText: 2024-present Harsh Parekh <harsh@ikigailabs.io>
#
# SPDX-License-Identifier: MIT

from __future__ import annotations

import io
import logging
import math
import time
from datetime import datetime
from enum import Enum
from http import HTTPStatus
from pathlib import Path
from typing import Any

import pandas as pd
import requests
from pydantic import BaseModel, Field

from ikigai.client.session import Session
from ikigai.utils.compatibility import Self
from ikigai.utils.named_mapping import NamedMapping
from ikigai.utils.protocols import Directory, DirectoryType

CHUNK_SIZE = int(50e6)  # 50 MB

logger = logging.getLogger("ikigai.components")


def __upload_data(
    session: Session,
    app_id: str,
    dataset_id: str,
    data: bytes,
    filename: str,
    chunk_size: int,
) -> None:
    num_parts = math.ceil(len(data) / chunk_size)

    resp = session.get(
        path="/component/get-dataset-multipart-upload-urls",
        params={
            "dataset_id": dataset_id,
            "project_id": app_id,
            "filename": filename,
            "number_of_parts": num_parts,
        },
    ).json()

    content_type = resp["content_type"]
    upload_urls: dict[int, str] = {
        int(chunk_idx): upload_url for chunk_idx, upload_url in resp["urls"].items()
    }
    upload_id = resp["upload_id"]
    etags: dict[int, str] = {}

    try:
        with requests.session() as request:
            request.headers.update(
                {"Content-Type": content_type, "Cache-Control": "no-cache"}
            )
            for chunk_idx, upload_url in upload_urls.items():
                chunk_start, chunk_end = (
                    (chunk_idx - 1) * chunk_size,
                    chunk_idx * chunk_size,
                )
                chunk = data[chunk_start:chunk_end]
                resp = request.put(url=upload_url, data=chunk)
                assert resp.status_code == HTTPStatus.OK

                # Get etags from response header
                etags[chunk_idx] = resp.headers.get("ETag")

    except Exception:
        session.post(
            path="/component/complete-dataset-multipart-upload",
            json={
                "dataset": {
                    "dataset_id": dataset_id,
                    "project_id": app_id,
                    "filename": filename,
                },
                "abort": True,
                "upload_id": upload_id,
            },
        )
        raise

    # Complete Dataset upload
    session.post(
        path="/component/complete-dataset-multipart-upload",
        json={
            "dataset": {
                "dataset_id": dataset_id,
                "project_id": app_id,
                "filename": filename,
            },
            "abort": False,
            "upload_id": upload_id,
            "etags": etags,
        },
    )


def _upload_data(
    session: Session, app_id: str, dataset_id: str, name: str, data: bytes
) -> None:
    assert data is not None
    filename = f"{name}.csv"

    __upload_data(
        session=session,
        app_id=app_id,
        dataset_id=dataset_id,
        data=data,
        filename=filename,
        chunk_size=CHUNK_SIZE,
    )

    upload_completion_time = time.time()
    session.get(
        path="/component/verify-dataset-upload",
        params={"dataset_id": dataset_id, "filename": filename},
    )

    dataset_status: str = "RUNNING"
    while dataset_status == "RUNNING":
        # Block thread while dataset is still being processed
        time.sleep(0.25)
        dataset_status = session.get(
            path="/component/confirm-dataset-upload",
            params={"dataset_id": dataset_id, "project_id": app_id},
        ).json()["status"]

    if dataset_status != "SUCCESS":
        error_msg = f"Dataset upload failed, upload ended with status {dataset_status}"
        raise RuntimeError(error_msg)

    dataset_logs = session.get(
        path="/component/get-dataset-log",
        params={"dataset_id": dataset_id, "project_id": app_id, "limit": 5},
    ).json()["dataset_log"]
    dataset_verified = [
        log
        for log in dataset_logs
        if log["status"] == "SUCCESS"
        and int(log["timestamp"]) > upload_completion_time
        and log["job_type"] == "UPLOAD_DATASET"
    ]
    if not dataset_verified:
        # TODO: Improve Error
        error_msg = "Dataset failed to verify"
        raise RuntimeError(error_msg, dataset_logs)


class DatasetBuilder:
    _app_id: str
    _name: str
    _data: bytes | None
    _directory: dict[str, str]
    __session: Session

    def __init__(self, session: Session, app_id: str) -> None:
        self.__session = session
        self._app_id = app_id
        self._name = ""
        self._data = None
        self._directory = {}

    def new(self, name: str) -> Self:
        self._name = name
        return self

    def df(self, data: pd.DataFrame) -> Self:
        buffer = io.BytesIO()
        data.to_csv(buffer, index_label=False, index=False)
        self._data = bytearray(buffer.getvalue())
        return self

    def csv(self, file: Path | str) -> Self:
        if isinstance(file, str):
            file = Path(file)
        with file.open("rb") as fp:
            self._data = bytearray(fp.read())
        return self

    def directory(self, directory: Directory) -> Self:
        self._directory = {
            "directory_id": directory.directory_id,
            "type": directory.type,
        }
        return self

    def build(self) -> Dataset:
        if self._data is None:
            error_msg = "Dataset is empty"
            raise ValueError(error_msg)

        resp = self.__session.post(
            path="/component/create-dataset",
            json={
                "dataset": {
                    "project_id": self._app_id,
                    "name": self._name,
                    "directory": self._directory,
                },
            },
        ).json()
        dataset_id = resp["dataset_id"]

        try:
            _upload_data(
                session=self.__session,
                app_id=self._app_id,
                dataset_id=dataset_id,
                name=self._name,
                data=self._data,
            )
        except Exception:
            # Delete created record and re-raise
            self.__session.post(
                path="/component/delete-dataset",
                json={
                    "dataset": {"project_id": self._app_id, "dataset_id": dataset_id}
                },
            )
            raise

        # Populate Dataset object
        resp = self.__session.get(
            path="/component/get-dataset", params={"dataset_id": dataset_id}
        ).json()
        dataset = Dataset.from_dict(data=resp["dataset"], session=self.__session)
        return dataset


class DataType(str, Enum):
    NUMERIC = "NUMERIC"
    TEXT = "TEXT"
    CATEGORICAL = "CATEGORICAL"
    TIME = "TIME"


class ColumnDataType(BaseModel):
    data_type: DataType
    data_formats: dict[str, str]


class Dataset(BaseModel):
    app_id: str = Field(validation_alias="project_id")
    dataset_id: str
    name: str
    filename: str
    file_extension: str
    data_types: dict[str, ColumnDataType]
    size: int
    created_at: datetime
    modified_at: datetime
    __session: Session

    @classmethod
    def from_dict(cls, data: dict, session: Session) -> Self:
        logger.debug("Creating a %s from %s", cls.__name__, data)
        self = cls.model_validate(data)
        self.__session = session
        return self

    def to_dict(self) -> dict:
        return {
            "dataset_id": self.dataset_id,
            "name": self.name,
            "filename": self.filename,
            "file_extension": self.file_extension,
            "data_types": self.data_types,
            "size": self.size,
            "created_at": self.created_at,
            "modified_at": self.modified_at,
        }

    def delete(self) -> None:
        self.__session.post(
            path="/component/delete-dataset",
            json={"dataset": {"dataset_id": self.dataset_id}},
        )
        return None

    def rename(self, name: str) -> Self:
        _ = self.__session.post(
            path="/component/edit-dataset",
            json={
                "dataset": {
                    "project_id": self.app_id,
                    "dataset_id": self.dataset_id,
                    "name": name,
                }
            },
        )
        # TODO: handle error case, currently it is a raise NotImplemented from Session
        self.name = name
        return self

    def move(self, directory: Directory) -> Self:
        _ = self.__session.post(
            path="/component/edit-dataset",
            json={
                "dataset": {
                    "project_id": self.app_id,
                    "dataset_id": self.dataset_id,
                    "directory": {
                        "directory_id": directory.directory_id,
                        "type": directory.type,
                    },
                }
            },
        )
        return self

    def df(self, **parser_options) -> pd.DataFrame:
        resp = self.__session.get(
            path="/component/get-dataset-download-url",
            params={
                "dataset_id": self.dataset_id,
                "project_id": self.app_id,
            },
        ).json()
        dataset_url = resp["url"]
        return pd.read_csv(dataset_url, **parser_options)

    def edit_data(self, data: pd.DataFrame) -> None:
        buffer = io.BytesIO()
        data.to_csv(buffer, index_label=False, index=False)

        _upload_data(
            session=self.__session,
            app_id=self.app_id,
            dataset_id=self.dataset_id,
            name=self.name,
            data=bytearray(buffer.getvalue()),
        )

    def describe(self) -> dict:
        response: dict[str, Any] = self.__session.get(
            path="/component/get-dataset",
            params={"dataset_id": self.dataset_id},
        ).json()

        return response


class DatasetDirectoryBuilder:
    _app_id: str
    _name: str
    _parent_id: str
    __session: Session

    def __init__(self, session: Session, app_id: str) -> None:
        self.__session = session
        self._app_id = app_id
        self._name = ""
        self._parent_id = ""

    def new(self, name: str) -> Self:
        self._name = name
        return self

    def parent(self, parent: Directory) -> Self:
        self._parent_id = parent.directory_id
        return self

    def build(self) -> DatasetDirectory:
        resp = self.__session.post(
            path="/component/create-dataset-directory",
            json={
                "directory": {
                    "name": self._name,
                    "project_id": self._app_id,
                    "parent_id": self._parent_id,
                }
            },
        ).json()
        directory_id = resp["directory_id"]
        resp = self.__session.get(
            path="/component/get-dataset-directory",
            params={"project_id": self._app_id, "directory_id": directory_id},
        ).json()

        directory = DatasetDirectory.from_dict(
            data=resp["directory"], session=self.__session
        )
        return directory


class DatasetDirectory(BaseModel):
    app_id: str = Field(validation_alias="project_id")
    directory_id: str
    name: str
    __session: Session

    @property
    def type(self) -> str:
        return DirectoryType.DATASET.value

    @classmethod
    def from_dict(cls, data: dict, session: Session) -> Self:
        logger.debug("Creating a %s from %s", cls.__name__, data)
        self = cls.model_validate(data)
        self.__session = session
        return self

    def directories(self) -> NamedMapping[Self]:
        resp = self.__session.get(
            path="/component/get-dataset-directories-for-project",
            params={"project_id": self.app_id, "directory_id": self.directory_id},
        ).json()
        directories = {
            directory.directory_id: directory
            for directory in (
                self.from_dict(data=directory_dict, session=self.__session)
                for directory_dict in resp["directories"]
            )
        }

        return NamedMapping(directories)

    def datasets(self) -> NamedMapping[Dataset]:
        resp = self.__session.get(
            path="/component/get-datasets-for-project",
            params={"project_id": self.app_id, "directory_id": self.directory_id},
        ).json()

        datasets = {
            dataset.dataset_id: dataset
            for dataset in (
                Dataset.from_dict(data=dataset_dict, session=self.__session)
                for dataset_dict in resp["datasets"]
            )
        }

        return NamedMapping(datasets)
