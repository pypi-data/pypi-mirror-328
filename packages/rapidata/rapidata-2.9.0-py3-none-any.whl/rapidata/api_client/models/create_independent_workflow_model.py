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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List
from rapidata.api_client.models.create_independent_workflow_model_workflow_config import CreateIndependentWorkflowModelWorkflowConfig
from typing import Optional, Set
from typing_extensions import Self

class CreateIndependentWorkflowModel(BaseModel):
    """
    Model for creating an independent workflow.
    """ # noqa: E501
    workflow_name: StrictStr = Field(description="The name of the workflow.", alias="workflowName")
    workflow_config: CreateIndependentWorkflowModelWorkflowConfig = Field(alias="workflowConfig")
    __properties: ClassVar[List[str]] = ["workflowName", "workflowConfig"]

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
        """Create an instance of CreateIndependentWorkflowModel from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of workflow_config
        if self.workflow_config:
            _dict['workflowConfig'] = self.workflow_config.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateIndependentWorkflowModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "workflowName": obj.get("workflowName"),
            "workflowConfig": CreateIndependentWorkflowModelWorkflowConfig.from_dict(obj["workflowConfig"]) if obj.get("workflowConfig") is not None else None
        })
        return _obj


