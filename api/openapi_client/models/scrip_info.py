# coding: utf-8

"""
    CubePlus Rest API Specifications

    Gateway API's

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr, field_validator
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ScripInfo(BaseModel):
    """
    ScripInfo
    """ # noqa: E501
    sym_id: Optional[StrictStr] = Field(default=None, description="Unique identifier of the symbol", alias="symId")
    invest_by: Optional[StrictStr] = Field(default=None, description="Investment type should be in qty or amount ", alias="investBy")
    qty: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="No of shares to buy or sell. For derivatives, pass the quantity by multiplying with lot size. Example: To buy 1 lot of NIFTY option, pass the quantity as 50.")
    amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Amount")
    __properties: ClassVar[List[str]] = ["symId", "investBy", "qty", "amount"]

    @field_validator('invest_by')
    def invest_by_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('qty', 'amount'):
            raise ValueError("must be one of enum values ('qty', 'amount')")
        return value

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ScripInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ScripInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "symId": obj.get("symId"),
            "investBy": obj.get("investBy"),
            "qty": obj.get("qty"),
            "amount": obj.get("amount")
        })
        return _obj


