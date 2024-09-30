# coding: utf-8

"""
    CubePlus Rest API Specifications

    Gateway API's

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401

from typing import Optional
from pydantic import BaseModel, Field, StrictStr, ValidationError, field_validator
from openapi_client.models.iou_message_response import IouMessageResponse
from openapi_client.models.positions_response import PositionsResponse
from typing import Union, Any, List, TYPE_CHECKING, Optional, Dict
from typing_extensions import Literal
from pydantic import StrictStr, Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

GETPOSITIONS200RESPONSE_ANY_OF_SCHEMAS = ["IouMessageResponse", "PositionsResponse"]

class GetPositions200Response(BaseModel):
    """
    GetPositions200Response
    """

    # data type: PositionsResponse
    anyof_schema_1_validator: Optional[PositionsResponse] = None
    # data type: IouMessageResponse
    anyof_schema_2_validator: Optional[IouMessageResponse] = None
    if TYPE_CHECKING:
        actual_instance: Optional[Union[IouMessageResponse, PositionsResponse]] = None
    else:
        actual_instance: Any = None
    any_of_schemas: List[str] = Literal[GETPOSITIONS200RESPONSE_ANY_OF_SCHEMAS]

    model_config = {
        "validate_assignment": True,
        "protected_namespaces": (),
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
    def actual_instance_must_validate_anyof(cls, v):
        instance = GetPositions200Response.model_construct()
        error_messages = []
        # validate data type: PositionsResponse
        if not isinstance(v, PositionsResponse):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PositionsResponse`")
        else:
            return v

        # validate data type: IouMessageResponse
        if not isinstance(v, IouMessageResponse):
            error_messages.append(f"Error! Input type `{type(v)}` is not `IouMessageResponse`")
        else:
            return v

        if error_messages:
            # no match
            raise ValueError("No match found when setting the actual_instance in GetPositions200Response with anyOf schemas: IouMessageResponse, PositionsResponse. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        # anyof_schema_1_validator: Optional[PositionsResponse] = None
        try:
            instance.actual_instance = PositionsResponse.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_2_validator: Optional[IouMessageResponse] = None
        try:
            instance.actual_instance = IouMessageResponse.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))

        if error_messages:
            # no match
            raise ValueError("No match found when deserializing the JSON string into GetPositions200Response with anyOf schemas: IouMessageResponse, PositionsResponse. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        to_json = getattr(self.actual_instance, "to_json", None)
        if callable(to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Dict:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        to_json = getattr(self.actual_instance, "to_json", None)
        if callable(to_json):
            return self.actual_instance.to_dict()
        else:
            return json.dumps(self.actual_instance)

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


