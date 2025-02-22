# SPDX-FileCopyrightText: 2024-present Harsh Parekh <harsh@ikigailabs.io>
#
# SPDX-License-Identifier: MIT

from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import BaseModel, EmailStr, Field

from ikigai import components
from ikigai.client.session import Session
from ikigai.utils.compatibility import Self
from ikigai.utils.named_mapping import NamedMapping
from ikigai.utils.protocols import Directory, DirectoryType


class AppBuilder:
    _name: str
    _description: str
    _directory: dict[str, str]
    _icon: str
    _images: list[str]
    __session: Session

    def __init__(self, session: Session) -> None:
        self.__session = session
        self._name = ""
        self._description = ""
        self._directory = {}
        self._icon = ""
        self._images = []

    def new(self, name: str) -> Self:
        self._name = name
        return self

    def description(self, description: str) -> Self:
        self._description = description
        return self

    def directory(self, directory: Directory) -> Self:
        self._directory = {
            "directory_id": directory.directory_id,
            "type": directory.type,
        }
        return self

    def build(self) -> App:
        resp = self.__session.post(
            path="/component/create-project",
            json={
                "project": {
                    "name": self._name,
                    "description": self._description,
                    "directory": self._directory,
                },
            },
        ).json()
        app_id = resp["project_id"]
        resp = self.__session.get(
            path="/component/get-project", params={"project_id": app_id}
        ).json()
        app = App.from_dict(data=resp["project"], session=self.__session)
        return app


class App(BaseModel):
    app_id: str = Field(validation_alias="project_id")
    name: str
    owner: EmailStr
    description: str
    created_at: datetime
    modified_at: datetime
    last_used_at: datetime
    __session: Session

    @classmethod
    def from_dict(cls, data: dict, session: Session) -> Self:
        self = cls.model_validate(data)
        self.__session = session
        return self

    """
    Operations on App
    """

    def to_dict(self) -> dict:
        return {
            "app_id": self.app_id,
            "name": self.name,
            "owner": self.owner,
            "description": self.description,
            "created_at": self.created_at,
            "modified_at": self.modified_at,
            "last_used_at": self.last_used_at,
        }

    def delete(self) -> None:
        self.__session.post(
            path="/component/delete-project",
            json={"project": {"project_id": self.app_id}},
        )
        return None

    def rename(self, name: str) -> Self:
        _ = self.__session.post(
            path="/component/edit-project",
            json={"project": {"project_id": self.app_id, "name": name}},
        )
        # TODO: handle error case, currently it is a raise NotImplemented from Session
        self.name = name
        return self

    def move(self, directory: Directory) -> Self:
        _ = self.__session.post(
            path="/component/edit-project",
            json={
                "project": {
                    "project_id": self.app_id,
                    "directory": {
                        "directory_id": directory.directory_id,
                        "type": directory.type,
                    },
                }
            },
        )
        return self

    def update_description(self, description: str) -> Self:
        _ = self.__session.post(
            path="/component/edit-project",
            json={"project": {"project_id": self.app_id, "description": description}},
        ).json()
        # TODO: handle error case, currently it is a raise NotImplemented from Session
        self.description = description
        return self

    def describe(self) -> dict:
        response: dict[str, Any] = self.__session.get(
            path="/component/get-components-for-project",
            params={"project_id": self.app_id},
        ).json()

        # Combine components information with app info
        return_value = {
            "app": self.to_dict(),
            "components": response["project_components"][self.app_id],
        }

        return return_value

    """
    Access Components in the App
    """

    def datasets(self) -> NamedMapping[components.Dataset]:
        resp = self.__session.get(
            path="/component/get-datasets-for-project",
            params={"project_id": self.app_id},
        ).json()
        datasets = {
            dataset.dataset_id: dataset
            for dataset in (
                components.Dataset.from_dict(data=dataset_dict, session=self.__session)
                for dataset_dict in resp["datasets"]
            )
        }

        return NamedMapping(datasets)

    @property
    def dataset(self) -> components.DatasetBuilder:
        return components.DatasetBuilder(session=self.__session, app_id=self.app_id)

    def dataset_directories(self) -> NamedMapping[components.DatasetDirectory]:
        resp = self.__session.get(
            path="/component/get-dataset-directories-for-project",
            params={"project_id": self.app_id},
        ).json()
        directories = {
            directory.directory_id: directory
            for directory in (
                components.DatasetDirectory.from_dict(
                    data=directory_dict, session=self.__session
                )
                for directory_dict in resp["directories"]
            )
        }

        return NamedMapping(directories)

    @property
    def dataset_directory(self) -> components.DatasetDirectoryBuilder:
        return components.DatasetDirectoryBuilder(
            session=self.__session, app_id=self.app_id
        )

    def flows(self) -> NamedMapping[components.Flow]:
        resp = self.__session.get(
            path="/component/get-pipelines-for-project",
            params={"project_id": self.app_id},
        ).json()

        flows = {
            flow.flow_id: flow
            for flow in (
                components.Flow.from_dict(data=flow_dict, session=self.__session)
                for flow_dict in resp["pipelines"]
            )
        }

        return NamedMapping(flows)

    @property
    def flow(self) -> components.FlowBuilder:
        return components.FlowBuilder(session=self.__session, app_id=self.app_id)

    def flow_directories(self) -> NamedMapping[components.FlowDirectory]:
        resp = self.__session.get(
            path="/component/get-pipeline-directories-for-project",
            params={"project_id": self.app_id},
        ).json()
        directories = {
            directory.directory_id: directory
            for directory in (
                components.FlowDirectory.from_dict(
                    data=directory_dict, session=self.__session
                )
                for directory_dict in resp["directories"]
            )
        }

        return NamedMapping(directories)

    @property
    def flow_directory(self) -> components.FlowDirectoryBuilder:
        return components.FlowDirectoryBuilder(
            session=self.__session, app_id=self.app_id
        )


class AppDirectory(BaseModel):
    directory_id: str
    name: str
    created_at: datetime
    modified_at: datetime
    __session: Session

    @property
    def type(self) -> str:
        return DirectoryType.APP.value

    @classmethod
    def from_dict(cls, data: dict, session: Session) -> Self:
        self = cls.model_validate(data)
        self.__session = session
        return self

    def directories(self) -> NamedMapping[Self]:
        resp = self.__session.get(
            path="/component/get-project-directories-for-user",
            params={"directory_id": self.directory_id},
        ).json()
        directories = {
            directory.directory_id: directory
            for directory in (
                self.from_dict(data=directory_dict, session=self.__session)
                for directory_dict in resp["directories"]
            )
        }

        return NamedMapping(directories)

    def apps(self) -> NamedMapping[App]:
        resp = self.__session.get(
            path="/component/get-projects-for-user",
            params={"directory_id": self.directory_id, "fetch_all": False},
        ).json()

        apps = {
            app.app_id: app
            for app in (
                App.from_dict(data=app_dict, session=self.__session)
                for app_dict in resp["projects"]
            )
        }

        return NamedMapping(apps)
