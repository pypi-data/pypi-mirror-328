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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class PreArrangedPairMakerConfigModel(BaseModel):
    """
    The PreArrangedPairMaker is used for completely random pairmaking from the beginning
    """ # noqa: E501
    t: StrictStr = Field(description="Discriminator value for PreArrangedPairMaker", alias="_t")
    pair_size: Optional[StrictInt] = Field(default=None, description="The pair size in comparisons.", alias="pairSize")
    __properties: ClassVar[List[str]] = ["_t", "pairSize"]

    @field_validator('t')
    def t_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['PreArrangedPairMaker']):
            raise ValueError("must be one of enum values ('PreArrangedPairMaker')")
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
        """Create an instance of PreArrangedPairMakerConfigModel from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PreArrangedPairMakerConfigModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_t": obj.get("_t") if obj.get("_t") is not None else 'PreArrangedPairMaker',
            "pairSize": obj.get("pairSize")
        })
        return _obj


