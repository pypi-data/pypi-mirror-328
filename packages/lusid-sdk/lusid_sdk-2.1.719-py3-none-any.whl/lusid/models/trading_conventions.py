# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    Contact: info@finbourne.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, Dict, Optional, Union
from pydantic.v1 import BaseModel, Field, StrictFloat, StrictInt

class TradingConventions(BaseModel):
    """
    Common Trading details for exchange traded instruments like Futures and Bonds  # noqa: E501
    """
    price_scale_factor: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="priceScaleFactor", description="The factor used to scale prices for the instrument. Currently used by LUSID when calculating cost  and notional amounts on transactions. Note this factor does not yet impact Valuation, PV, exposure,  all of which use the scale factor attached to the price quotes in the QuoteStore.  Must be positive and defaults to 1 if not set.")
    minimum_order_size: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="minimumOrderSize", description="The Minimum Order Size  Must be non-negative and defaults to 0 if not set.")
    minimum_order_increment: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="minimumOrderIncrement", description="The Minimum Order Increment  Must be non-negative and defaults to 0 if not set.")
    __properties = ["priceScaleFactor", "minimumOrderSize", "minimumOrderIncrement"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def __str__(self):
        """For `print` and `pprint`"""
        return pprint.pformat(self.dict(by_alias=False))

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> TradingConventions:
        """Create an instance of TradingConventions from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TradingConventions:
        """Create an instance of TradingConventions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TradingConventions.parse_obj(obj)

        _obj = TradingConventions.parse_obj({
            "price_scale_factor": obj.get("priceScaleFactor"),
            "minimum_order_size": obj.get("minimumOrderSize"),
            "minimum_order_increment": obj.get("minimumOrderIncrement")
        })
        return _obj
