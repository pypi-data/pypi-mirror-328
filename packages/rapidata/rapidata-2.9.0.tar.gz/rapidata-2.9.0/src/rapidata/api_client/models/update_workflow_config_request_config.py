# coding: utf-8

"""
    Rapidata.Dataset

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from rapidata.api_client.models.compare_workflow_config_model import CompareWorkflowConfigModel
from rapidata.api_client.models.simple_workflow_config_model import SimpleWorkflowConfigModel
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

UPDATEWORKFLOWCONFIGREQUESTCONFIG_ONE_OF_SCHEMAS = ["CompareWorkflowConfigModel", "SimpleWorkflowConfigModel"]

class UpdateWorkflowConfigRequestConfig(BaseModel):
    """
    The new workflow configuration.
    """
    # data type: CompareWorkflowConfigModel
    oneof_schema_1_validator: Optional[CompareWorkflowConfigModel] = None
    # data type: SimpleWorkflowConfigModel
    oneof_schema_2_validator: Optional[SimpleWorkflowConfigModel] = None
    actual_instance: Optional[Union[CompareWorkflowConfigModel, SimpleWorkflowConfigModel]] = None
    one_of_schemas: Set[str] = { "CompareWorkflowConfigModel", "SimpleWorkflowConfigModel" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    discriminator_value_class_map: Dict[str, str] = {
    }

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = UpdateWorkflowConfigRequestConfig.model_construct()
        error_messages = []
        match = 0
        # validate data type: CompareWorkflowConfigModel
        if not isinstance(v, CompareWorkflowConfigModel):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CompareWorkflowConfigModel`")
        else:
            match += 1
        # validate data type: SimpleWorkflowConfigModel
        if not isinstance(v, SimpleWorkflowConfigModel):
            error_messages.append(f"Error! Input type `{type(v)}` is not `SimpleWorkflowConfigModel`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in UpdateWorkflowConfigRequestConfig with oneOf schemas: CompareWorkflowConfigModel, SimpleWorkflowConfigModel. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in UpdateWorkflowConfigRequestConfig with oneOf schemas: CompareWorkflowConfigModel, SimpleWorkflowConfigModel. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into CompareWorkflowConfigModel
        try:
            instance.actual_instance = CompareWorkflowConfigModel.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into SimpleWorkflowConfigModel
        try:
            instance.actual_instance = SimpleWorkflowConfigModel.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into UpdateWorkflowConfigRequestConfig with oneOf schemas: CompareWorkflowConfigModel, SimpleWorkflowConfigModel. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into UpdateWorkflowConfigRequestConfig with oneOf schemas: CompareWorkflowConfigModel, SimpleWorkflowConfigModel. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], CompareWorkflowConfigModel, SimpleWorkflowConfigModel]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


