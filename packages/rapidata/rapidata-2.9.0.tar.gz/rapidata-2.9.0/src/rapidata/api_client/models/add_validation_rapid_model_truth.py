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
from rapidata.api_client.models.attach_category_truth import AttachCategoryTruth
from rapidata.api_client.models.bounding_box_truth import BoundingBoxTruth
from rapidata.api_client.models.compare_truth import CompareTruth
from rapidata.api_client.models.empty_validation_truth import EmptyValidationTruth
from rapidata.api_client.models.line_truth import LineTruth
from rapidata.api_client.models.locate_box_truth import LocateBoxTruth
from rapidata.api_client.models.named_entity_truth import NamedEntityTruth
from rapidata.api_client.models.polygon_truth import PolygonTruth
from rapidata.api_client.models.scrub_truth import ScrubTruth
from rapidata.api_client.models.transcription_truth import TranscriptionTruth
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

ADDVALIDATIONRAPIDMODELTRUTH_ONE_OF_SCHEMAS = ["AttachCategoryTruth", "BoundingBoxTruth", "CompareTruth", "EmptyValidationTruth", "LineTruth", "LocateBoxTruth", "NamedEntityTruth", "PolygonTruth", "ScrubTruth", "TranscriptionTruth"]

class AddValidationRapidModelTruth(BaseModel):
    """
    The ground truth for the rapid.
    """
    # data type: TranscriptionTruth
    oneof_schema_1_validator: Optional[TranscriptionTruth] = None
    # data type: ScrubTruth
    oneof_schema_2_validator: Optional[ScrubTruth] = None
    # data type: PolygonTruth
    oneof_schema_3_validator: Optional[PolygonTruth] = None
    # data type: NamedEntityTruth
    oneof_schema_4_validator: Optional[NamedEntityTruth] = None
    # data type: LocateBoxTruth
    oneof_schema_5_validator: Optional[LocateBoxTruth] = None
    # data type: LineTruth
    oneof_schema_6_validator: Optional[LineTruth] = None
    # data type: EmptyValidationTruth
    oneof_schema_7_validator: Optional[EmptyValidationTruth] = None
    # data type: CompareTruth
    oneof_schema_8_validator: Optional[CompareTruth] = None
    # data type: AttachCategoryTruth
    oneof_schema_9_validator: Optional[AttachCategoryTruth] = None
    # data type: BoundingBoxTruth
    oneof_schema_10_validator: Optional[BoundingBoxTruth] = None
    actual_instance: Optional[Union[AttachCategoryTruth, BoundingBoxTruth, CompareTruth, EmptyValidationTruth, LineTruth, LocateBoxTruth, NamedEntityTruth, PolygonTruth, ScrubTruth, TranscriptionTruth]] = None
    one_of_schemas: Set[str] = { "AttachCategoryTruth", "BoundingBoxTruth", "CompareTruth", "EmptyValidationTruth", "LineTruth", "LocateBoxTruth", "NamedEntityTruth", "PolygonTruth", "ScrubTruth", "TranscriptionTruth" }

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
        instance = AddValidationRapidModelTruth.model_construct()
        error_messages = []
        match = 0
        # validate data type: TranscriptionTruth
        if not isinstance(v, TranscriptionTruth):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TranscriptionTruth`")
        else:
            match += 1
        # validate data type: ScrubTruth
        if not isinstance(v, ScrubTruth):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ScrubTruth`")
        else:
            match += 1
        # validate data type: PolygonTruth
        if not isinstance(v, PolygonTruth):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PolygonTruth`")
        else:
            match += 1
        # validate data type: NamedEntityTruth
        if not isinstance(v, NamedEntityTruth):
            error_messages.append(f"Error! Input type `{type(v)}` is not `NamedEntityTruth`")
        else:
            match += 1
        # validate data type: LocateBoxTruth
        if not isinstance(v, LocateBoxTruth):
            error_messages.append(f"Error! Input type `{type(v)}` is not `LocateBoxTruth`")
        else:
            match += 1
        # validate data type: LineTruth
        if not isinstance(v, LineTruth):
            error_messages.append(f"Error! Input type `{type(v)}` is not `LineTruth`")
        else:
            match += 1
        # validate data type: EmptyValidationTruth
        if not isinstance(v, EmptyValidationTruth):
            error_messages.append(f"Error! Input type `{type(v)}` is not `EmptyValidationTruth`")
        else:
            match += 1
        # validate data type: CompareTruth
        if not isinstance(v, CompareTruth):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CompareTruth`")
        else:
            match += 1
        # validate data type: AttachCategoryTruth
        if not isinstance(v, AttachCategoryTruth):
            error_messages.append(f"Error! Input type `{type(v)}` is not `AttachCategoryTruth`")
        else:
            match += 1
        # validate data type: BoundingBoxTruth
        if not isinstance(v, BoundingBoxTruth):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BoundingBoxTruth`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in AddValidationRapidModelTruth with oneOf schemas: AttachCategoryTruth, BoundingBoxTruth, CompareTruth, EmptyValidationTruth, LineTruth, LocateBoxTruth, NamedEntityTruth, PolygonTruth, ScrubTruth, TranscriptionTruth. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in AddValidationRapidModelTruth with oneOf schemas: AttachCategoryTruth, BoundingBoxTruth, CompareTruth, EmptyValidationTruth, LineTruth, LocateBoxTruth, NamedEntityTruth, PolygonTruth, ScrubTruth, TranscriptionTruth. Details: " + ", ".join(error_messages))
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

        # deserialize data into TranscriptionTruth
        try:
            instance.actual_instance = TranscriptionTruth.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ScrubTruth
        try:
            instance.actual_instance = ScrubTruth.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into PolygonTruth
        try:
            instance.actual_instance = PolygonTruth.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into NamedEntityTruth
        try:
            instance.actual_instance = NamedEntityTruth.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into LocateBoxTruth
        try:
            instance.actual_instance = LocateBoxTruth.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into LineTruth
        try:
            instance.actual_instance = LineTruth.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into EmptyValidationTruth
        try:
            instance.actual_instance = EmptyValidationTruth.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into CompareTruth
        try:
            instance.actual_instance = CompareTruth.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into AttachCategoryTruth
        try:
            instance.actual_instance = AttachCategoryTruth.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into BoundingBoxTruth
        try:
            instance.actual_instance = BoundingBoxTruth.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into AddValidationRapidModelTruth with oneOf schemas: AttachCategoryTruth, BoundingBoxTruth, CompareTruth, EmptyValidationTruth, LineTruth, LocateBoxTruth, NamedEntityTruth, PolygonTruth, ScrubTruth, TranscriptionTruth. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into AddValidationRapidModelTruth with oneOf schemas: AttachCategoryTruth, BoundingBoxTruth, CompareTruth, EmptyValidationTruth, LineTruth, LocateBoxTruth, NamedEntityTruth, PolygonTruth, ScrubTruth, TranscriptionTruth. Details: " + ", ".join(error_messages))
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

    def to_dict(self) -> Optional[Union[Dict[str, Any], AttachCategoryTruth, BoundingBoxTruth, CompareTruth, EmptyValidationTruth, LineTruth, LocateBoxTruth, NamedEntityTruth, PolygonTruth, ScrubTruth, TranscriptionTruth]]:
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


