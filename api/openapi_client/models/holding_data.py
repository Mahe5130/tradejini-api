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


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool
from pydantic import Field
from openapi_client.models.holdings import Holdings
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class HoldingData(BaseModel):
    """
    HoldingData
    """ # noqa: E501
    holdings: Optional[List[Holdings]] = None
    has_non_poa_record: Optional[StrictBool] = Field(default=None, alias="hasNonPoaRecord")
    __properties: ClassVar[List[str]] = ["holdings", "hasNonPoaRecord"]

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
        """Create an instance of HoldingData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in holdings (list)
        _items = []
        if self.holdings:
            for _item in self.holdings:
                if _item:
                    _items.append(_item.to_dict())
            _dict['holdings'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of HoldingData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "holdings": [Holdings.from_dict(_item) for _item in obj.get("holdings")] if obj.get("holdings") is not None else None,
            "hasNonPoaRecord": obj.get("hasNonPoaRecord")
        })
        return _obj


