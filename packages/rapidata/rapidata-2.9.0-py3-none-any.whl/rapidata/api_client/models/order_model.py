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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class OrderModel(BaseModel):
    """
    OrderModel
    """ # noqa: E501
    id: StrictStr
    pipeline_id: StrictStr = Field(alias="pipelineId")
    order_date: Optional[datetime] = Field(default=None, alias="orderDate")
    customer_mail: StrictStr = Field(alias="customerMail")
    state: StrictStr
    order_name: StrictStr = Field(alias="orderName")
    is_public: StrictBool = Field(alias="isPublic")
    __properties: ClassVar[List[str]] = ["id", "pipelineId", "orderDate", "customerMail", "state", "orderName", "isPublic"]

    @field_validator('state')
    def state_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['Created', 'Submitted', 'ManualReview', 'Processing', 'Paused', 'Completed', 'Cancelled', 'Failed']):
            raise ValueError("must be one of enum values ('Created', 'Submitted', 'ManualReview', 'Processing', 'Paused', 'Completed', 'Cancelled', 'Failed')")
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
        """Create an instance of OrderModel from a JSON string"""
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
        # set to None if order_date (nullable) is None
        # and model_fields_set contains the field
        if self.order_date is None and "order_date" in self.model_fields_set:
            _dict['orderDate'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OrderModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "pipelineId": obj.get("pipelineId"),
            "orderDate": obj.get("orderDate"),
            "customerMail": obj.get("customerMail"),
            "state": obj.get("state"),
            "orderName": obj.get("orderName"),
            "isPublic": obj.get("isPublic")
        })
        return _obj


