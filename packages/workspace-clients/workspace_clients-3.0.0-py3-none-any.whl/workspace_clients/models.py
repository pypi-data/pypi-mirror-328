from __future__ import annotations

import json
from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Dict, List, Optional
from uuid import UUID

from annotated_types import MaxLen
from clients_core.exceptions import ClientException
from pydantic import (
    ConfigDict,
    Field,
    PrivateAttr,
    field_validator,
    BaseModel as PydanticBaseModel,
)

if TYPE_CHECKING:
    from .assets_client import WorkspaceServiceAssetsClient
    from .containers_client import WorkspaceServiceContainersClient


class BaseModel(PydanticBaseModel):
    def dump(self) -> dict:
        return json.loads(self.model_dump_json(by_alias=True))

    @field_validator("name", "description", mode="before", check_fields=False)
    def _trim_max_length(cls, value, info):  # type: ignore
        if value:
            metadata = cls.model_fields[info.field_name].metadata
            filter_cond = lambda v: isinstance(v, MaxLen)

            if meta := next(filter(filter_cond, metadata), None):
                return value[: meta.max_length]

        return value

    model_config = ConfigDict(use_enum_values=True)


class LocationSearchType(Enum):
    SINGLE_LEVEL = "singleLevel"
    SUBTREE = "subtree"


class AssetType(Enum):
    ANALYTIC = "Analytic"
    ANALYTIC_DATASET = "Analytic Dataset"
    ANALYTIC_PACKAGE = "Analytic Package"
    ANALYTIC_WORKBENCH_PROJECT = "Analytics Workbench Project"
    CARD = "Card"
    COHORT = "Cohort"
    COHORT_PREVIEW = "Cohort Preview"
    CDM_9 = "Core Diabetes Model v9.0"
    CDM_9_5 = "Core Diabetes Model v9.5"
    COVARIATE_TEMPLATE = "Covariate Template"
    DASHBOARD = "Dashboard"
    DATA_ON_DEMAND = "Data on Demand"
    DATA_SLICE = "Data Slice"
    DATASET_DISTRIBUTION = "Dataset Distribution"
    DESCRIPTIVE_ANALYTIC = "Descriptive Analytic"
    DOCUMENT = "Document"
    EVIDENCE_PLANNER_ASSET = "Evidence Planner Asset"
    EXPORT = "Export"
    GENOMIC_QUERY = "Genomic Query"
    GENOMIC_VARIANT_LIST = "Genomic Variant List"
    GROUPED_CODELIST = "Grouped Codelist"
    INTERACTIVE_REPORT = "Interactive Report"
    LINK = "Link"
    NOTEBOOK = "Notebook"
    PUBLISHED_DASHBOARD = "Published Dashboard"
    PUBLISHED_INTERACTIVE_REPORT = "Published Interactive Report"
    RECRUITMENT = "Recruitment"
    REPORT = "Report"
    SCIENTIFIC_REPORT = "Scientific Report"
    VARIANT_LIST = "Variant List"
    VISUALIZATION = "Visualisation"
    WORKFLOW = "Workflow"


class ContainerEmbed(Enum):
    CHILDREN = "children"
    PARENT = "parent"
    SHARED_WITH = "sharedWith"


class AssetEmbed(Enum):
    PARENT = "parent"
    METADATA = "metadata"
    DATASET_INFO = "datasetInfo"


class AssetModel(BaseModel):
    type: AssetType
    name: Optional[str] = Field(None, max_length=100)
    id: Optional[UUID] = None
    parent: Optional[dict] = None
    parentAssetId: Optional[UUID] = None
    subtype: Optional[str] = None
    isHidden: Optional[bool] = None
    sentByUserId: Optional[str] = None
    datasetInfo: Optional[List[dict]] = None
    metadata: Optional[Dict[str, str]] = None
    description: Optional[str] = Field(None, max_length=500)
    isFavourite: Optional[bool] = None
    rights: Optional[dict] = None
    createdByUserId: Optional[UUID] = None
    isShared: Optional[bool] = None
    created: Optional[datetime] = None
    updated: Optional[datetime] = None

    _assets_client: Optional[WorkspaceServiceAssetsClient] = PrivateAttr(default=None)

    def delete(self) -> bool:
        if self._assets_client is None:  # type: ignore
            message = (
                "Can not perform AssetMode.delete operation."
                "No instance of WorkspaceServiceAssetsClient has been provided to this model."
                "Please use WorkspaceServiceAssetsClient.delete function instead"
            )

            raise ClientException(message)
        return self._assets_client.delete(self.id)  # type: ignore


class ContainerModel(BaseModel):
    name: str = Field(..., max_length=100)
    id: Optional[UUID] = None
    type: Optional[str] = "standard"
    description: Optional[str] = Field(None, max_length=500)
    parent: Optional[dict] = None
    children: Optional[List[dict]] = None
    rights: Optional[dict] = None
    isFavourite: Optional[bool] = None
    isShared: Optional[bool] = None
    sharedWith: Optional[dict] = None
    totalDescendantAssets: Optional[int] = None
    createdByUserId: Optional[UUID] = None
    created: Optional[datetime] = None
    updated: Optional[datetime] = None

    _containers_client: Optional[WorkspaceServiceContainersClient] = PrivateAttr(
        default=None
    )

    def delete(self) -> bool:
        if self._containers_client is None:  # type: ignore
            message = (
                "Can not perform ContainerModel.delete operation. "
                "No instance of WorkspaceServiceContainersClient has been provided to this model."
                "Please use WorkspaceServiceContainersClient.delete function instead"
            )
            raise ClientException(message)
        return self._containers_client.delete(self.id)  # type: ignore
