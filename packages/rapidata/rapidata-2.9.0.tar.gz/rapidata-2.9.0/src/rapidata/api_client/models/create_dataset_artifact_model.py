# coding: utf-8

"""
    Rapidata.Dataset

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List
from rapidata.api_client.models.create_dataset_artifact_model_dataset import CreateDatasetArtifactModelDataset
from typing import Optional, Set
from typing_extensions import Self

class CreateDatasetArtifactModel(BaseModel):
    """
    Model for creating a dataset artifact
    """ # noqa: E501
    t: StrictStr = Field(description="Discriminator value for CreateDatasetArtifactModel", alias="_t")
    identifier: StrictStr = Field(description="The identifier of the artifact")
    dataset: CreateDatasetArtifactModelDataset
    __properties: ClassVar[List[str]] = ["_t", "identifier", "dataset"]

    @field_validator('t')
    def t_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['CreateDatasetArtifactModel']):
            raise ValueError("must be one of enum values ('CreateDatasetArtifactModel')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of CreateDatasetArtifactModel from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of dataset
        if self.dataset:
            _dict['dataset'] = self.dataset.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateDatasetArtifactModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_t": obj.get("_t") if obj.get("_t") is not None else 'CreateDatasetArtifactModel',
            "identifier": obj.get("identifier"),
            "dataset": CreateDatasetArtifactModelDataset.from_dict(obj["dataset"]) if obj.get("dataset") is not None else None
        })
        return _obj


