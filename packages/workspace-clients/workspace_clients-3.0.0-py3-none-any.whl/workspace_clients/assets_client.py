import warnings
from typing import Any, Dict, List
from uuid import UUID

from clients_core.service_clients import E360ServiceClient
from pydantic import TypeAdapter
from requests import Response

from .models import AssetEmbed, AssetModel, AssetType


class WorkspaceServiceAssetsClient(E360ServiceClient):
    """
    A client for the asset endpoint of workspace service
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

    def get_assets(
        self,
        fields: List[str] = None,
        type_: AssetType = None,
        embed: List[AssetEmbed] = None,
        metadata_key: str = "",
        metadata_value: str = "",
        sort: List[str] = None,
        params: Dict = None,
        **kwargs: Any,
    ) -> List[AssetModel]:
        """
        Creates a get request for the assets endpoint, returning the assets of the current user.
        By default all the assets will be returned without any pagination.

        Returns:
            list: a list of assets for the users that matched the provided filters

        Raises:
            clients_core.exceptions.HttpResponseError: on server response errors.
        """
        if not fields:
            fields = []
        if not embed:
            embed = []
        if not params:
            params = {}
        if not sort:
            sort = ["-created"]

        params["sort"] = ",".join(s for s in sort)
        if type_:
            params["type"] = type_.value
        if fields:
            params["fields"] = ",".join(fields)
        if embed:
            params["embed"] = ",".join(e.value for e in embed)
        if metadata_key:
            params["metadataKey"] = metadata_key
            params["metadataValue"] = metadata_value
        response = self.client.get(
            "", params=params, headers=self.service_headers, raises=True, **kwargs
        )
        return self._response_to_models(response)

    def delete(self, id_: UUID, **kwargs: AssetModel) -> bool:
        """
        Delete the specified asset, if it exists

        Returns:
            bool: True / False for successful / failed requests

        Raises:
            clients_core.exceptions.HttpResponseError: on server response errors.
        """
        response = self.client.delete(
            str(id_), headers=self.service_headers, raises=True, **kwargs
        )
        return response.ok

    def get_by_id(self, id_: UUID, **kwargs: Any) -> AssetModel:
        """
        Retrieve a single asset using its id

        Returns:
            AssetModel: The result asset matching the id provided

        Raises:
            clients_core.exceptions.HttpResponseError: on server response errors.
        """
        response = self.client.get(
            str(id_), headers=self.service_headers, raises=True, **kwargs
        )
        return self._response_to_model(response)

    def create(self, asset: AssetModel, **kwargs: Any) -> AssetModel:
        """
        Create a new asset in workspaces

        Returns:
            AssetModel: The newly created asset, as returned by workspaces API

        Raises:
            clients_core.exceptions.HttpResponseError: on server response errors.
        """
        response = self.client.post(
            "", json=asset.dump(), headers=self.service_headers, raises=True, **kwargs
        )
        return self._response_to_model(response)

    def update(self, asset_id: UUID, asset: AssetModel, **kwargs: Any) -> AssetModel:
        """
        Updates the asset with new values
        Args:
            asset_id: the id of the asset
            asset: AssetModel object with which we update the asset

        Returns:
            AssetModel object with updated values
        """

        response = self.client.put(
            str(asset_id),
            json=asset.dump(),
            headers=self.service_headers,
            raises=True,
            **kwargs,
        )
        return self._response_to_model(response)

    def patch_asset(
        self, id_: UUID, patch_document: List[Dict], **kwargs: Any
    ) -> AssetModel:
        warnings.warn(".patch_asset deprecated, use .modify", DeprecationWarning)
        return self.modify(id_, patch_document, **kwargs)

    def modify(
        self, id_: UUID, patch_document: List[Dict], **kwargs: Any
    ) -> AssetModel:
        """
        Make changes to an existing asset. A JSON patch document needs to be passed to specify the changes that need to apply

        Returns:
            AssetModel: The updated asset, as returned by workspaces API

        Raises:
            clients_core.exceptions.HttpResponseError: on server response errors.
        """
        response = self.client.patch(
            str(id_),
            json=patch_document,
            raises=True,
            headers=self.service_headers,
            **kwargs,
        )
        return self._response_to_model(response)

    def _response_to_models(self, response: Response) -> List[AssetModel]:
        response_json = response.json()["resources"]
        type_adapter = TypeAdapter(List[AssetModel])
        instances = type_adapter.validate_python(response_json)
        for instance in instances:
            instance._assets_client = self
        return instances

    def _response_to_model(self, response: Response) -> AssetModel:
        response_json = response.json()
        instance = AssetModel.model_validate(response_json)
        instance._assets_client = self
        return instance
