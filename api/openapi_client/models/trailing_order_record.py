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

class TrailingOrderRecord(BaseModel):
    """
    TrailingOrderRecord
    """ # noqa: E501
    sym_id: Optional[StrictStr] = Field(default=None, alias="symId")
    order_id: Optional[StrictStr] = Field(default=None, alias="orderId")
    side: Optional[StrictStr] = None
    type: Optional[StrictStr] = None
    product: Optional[StrictStr] = None
    validity: Optional[StrictStr] = None
    qty: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Order quantity")
    limit_price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="limitPrice")
    target_price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Target order or Profit order price", alias="targetPrice")
    trailing_stop_price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Trailing stop loss price.", alias="trailingStopPrice")
    reason: Optional[StrictStr] = None
    price_factor: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Used for pnl calculations. PriceFactor:(General Numerator * Price Numerator)/(General Denominator * Price Denopminator)", alias="priceFactor")
    multiplier: Optional[Union[StrictFloat, StrictInt]] = None
    trig_price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="This is required only for stoploss limit and stoploss market orders", alias="trigPrice")
    status: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["symId", "orderId", "side", "type", "product", "validity", "qty", "limitPrice", "targetPrice", "trailingStopPrice", "reason", "priceFactor", "multiplier", "trigPrice", "status"]

    @field_validator('side')
    def side_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('buy', 'sell'):
            raise ValueError("must be one of enum values ('buy', 'sell')")
        return value

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('limit', 'market', 'stoplimit', 'stopmarket'):
            raise ValueError("must be one of enum values ('limit', 'market', 'stoplimit', 'stopmarket')")
        return value

    @field_validator('product')
    def product_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('delivery', 'normal', 'intraday', 'cover', 'bracket'):
            raise ValueError("must be one of enum values ('delivery', 'normal', 'intraday', 'cover', 'bracket')")
        return value

    @field_validator('validity')
    def validity_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('day', 'ioc', 'eos', 'gtc'):
            raise ValueError("must be one of enum values ('day', 'ioc', 'eos', 'gtc')")
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
        """Create an instance of TrailingOrderRecord from a JSON string"""
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
        """Create an instance of TrailingOrderRecord from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "symId": obj.get("symId"),
            "orderId": obj.get("orderId"),
            "side": obj.get("side"),
            "type": obj.get("type"),
            "product": obj.get("product"),
            "validity": obj.get("validity"),
            "qty": obj.get("qty"),
            "limitPrice": obj.get("limitPrice"),
            "targetPrice": obj.get("targetPrice"),
            "trailingStopPrice": obj.get("trailingStopPrice"),
            "reason": obj.get("reason"),
            "priceFactor": obj.get("priceFactor"),
            "multiplier": obj.get("multiplier"),
            "trigPrice": obj.get("trigPrice"),
            "status": obj.get("status")
        })
        return _obj


