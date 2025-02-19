from typing import Any, Dict, List
from uuid import UUID

from clients_core.service_clients import E360ServiceClient
from pydantic import TypeAdapter
from requests import Response

from .models import ContainerEmbed, ContainerModel, LocationSearchType


class WorkspaceServiceContainersClient(E360ServiceClient):
    """
    A client for the containers endpoint of workspace service
    Subclasses dataclass `clients_core.service_clients.E360ServiceClient`.

    Args:
        client (clients_core.rest_client.RestClient): an instance of a rest client
        user_id (str): the user_id guid
        correlation_id (str): the correlation-id to be passed on the request headers

    """

    service_endpoint: str = ""
    extra_headers: Dict = {
        "accept": "application/json",
        "content-type": "application/json",
    }

    def create(self, model: ContainerModel, **kwargs: Any) -> ContainerModel:
        """
        Creates a POST request for the containers endpoint, to allow the creation of a new container.

        Returns:
            ContainerModel: the newly created Container instance
        Raises:
            clients_core.exceptions.HttpResponseError: on server response errors.
        """

        response = self.client.post(
            "", json=model.dump(), headers=self.service_headers, raises=True, **kwargs
        )
        return self._response_to_model(response)

    def update(
        self, cont_id: UUID, model: ContainerModel, **kwargs: Any
    ) -> ContainerModel:
        """
        Updates the Container with provided model
        Args:
            cont_id: the id of the container
            model: ContainerModel object with which we are updating the container

        Returns:
            ContainerModel object with updated container values
        """
        response = self.client.put(
            str(cont_id),
            json=model.dump(),
            headers=self.service_headers,
            raises=True,
            **kwargs,
        )
        return self._response_to_model(response)

    def modify(self, cont_id: UUID, data: List[dict], **kwargs: Any) -> ContainerModel:
        """
        Modifies fields in the container
        Args:
            cont_id: the id of the container
            data: List of dictionaries containing fields and values to modify

        Returns:
            ContainerModel object with modified container values
        """

        response = self.client.patch(
            str(cont_id), json=data, headers=self.service_headers, raises=True, **kwargs
        )
        return self._response_to_model(response)

    def delete(self, cont_id: UUID, **kwargs: Any) -> bool:
        """
        Delete the specified container, if it exists

        Returns:
            bool: True / False for successful / failed requests

        Raises:
            clients_core.exceptions.HttpResponseError: on server response errors.
        """
        response = self.client.delete(
            str(cont_id), headers=self.service_headers, raises=True, **kwargs
        )
        return response.ok

    def get_by_id(
        self,
        id_: UUID,
        all_ancestors: bool = False,
        all_descendants: bool = False,
        embed: List[ContainerEmbed] = None,
        params: dict = {},
        **kwargs: Any,
    ) -> ContainerModel:
        """
        Retrieve a single container using its id. Can specify which fields should be returned using embed, and whether to include ancestors or descedants

        Returns:
            ContainerModel: The container matching the id provided

        Raises:
            clients_core.exceptions.HttpResponseError: on server response errors.
        """
        if embed:
            params["embed"] = ",".join(e.value for e in embed)
        if all_ancestors:
            params["allAncestors"] = all_ancestors
        if all_descendants:
            params["allDescendants"] = all_descendants
        response = self.client.get(
            str(id_), params=params, headers=self.service_headers, raises=True, **kwargs
        )
        return self._response_to_model(response)

    def get(
        self,
        name: str = None,
        location_search_type: LocationSearchType = LocationSearchType.SINGLE_LEVEL,
        embed: List[ContainerEmbed] = None,
        sort: List[str] = ["-created"],
        params: dict = {},
        **kwargs: Any,
    ) -> List[ContainerModel]:
        params["sort"] = ",".join(s for s in sort)
        """
        Creates a get request for the containers endpoint, returning the containers of the current user.
        By default all the containers will be returned without any pagination.

        Returns:
            list: a list of containers for the user that matched the provided filters

        Raises:
            clients_core.exceptions.HttpResponseError: on server response errors.
        """

        if name:
            params["name"] = name
        if location_search_type:
            params["locationSearchType"] = location_search_type.value
        if embed:
            params["embed"] = ",".join(e.value for e in embed)

        response = self.client.get(
            "", params=params, headers=self.service_headers, raises=True, **kwargs
        )
        return self._response_to_models(response)

    def _response_to_models(self, response: Response) -> List[ContainerModel]:
        response_json = response.json()["resources"]
        type_adapter = TypeAdapter(List[ContainerModel])
        instances = type_adapter.validate_python(response_json)
        for instance in instances:
            instance._containers_client = self
        return instances

    def _response_to_model(self, response: Response) -> ContainerModel:
        response_json = response.json()
        instance = ContainerModel.model_validate(response_json)
        instance._containers_client = self
        return instance
