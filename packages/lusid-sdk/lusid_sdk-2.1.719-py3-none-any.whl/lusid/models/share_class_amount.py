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

class ShareClassAmount(BaseModel):
    """
    ShareClassAmount
    """
    fund_currency_amount: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="fundCurrencyAmount", description="The value of the amount in the fund currency.")
    share_class_currency_amount: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="shareClassCurrencyAmount", description="The value of the amount in the share class currency.")
    __properties = ["fundCurrencyAmount", "shareClassCurrencyAmount"]

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
    def from_json(cls, json_str: str) -> ShareClassAmount:
        """Create an instance of ShareClassAmount from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ShareClassAmount:
        """Create an instance of ShareClassAmount from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ShareClassAmount.parse_obj(obj)

        _obj = ShareClassAmount.parse_obj({
            "fund_currency_amount": obj.get("fundCurrencyAmount"),
            "share_class_currency_amount": obj.get("shareClassCurrencyAmount")
        })
        return _obj
