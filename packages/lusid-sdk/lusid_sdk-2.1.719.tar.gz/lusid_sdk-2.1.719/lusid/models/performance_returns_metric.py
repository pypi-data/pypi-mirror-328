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


from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictBool, StrictStr

class PerformanceReturnsMetric(BaseModel):
    """
    The request used in the AggregatedReturns.  # noqa: E501
    """
    type: Optional[StrictStr] = Field(None, description="The type of the metric. Default to Return")
    window: Optional[StrictStr] = Field(None, description="The given metric for the calculation i.e. 1Y, 1D.")
    allow_partial: Optional[StrictBool] = Field(None, alias="allowPartial", description="Bool if the metric is allowed partial results. Default to false.")
    annualised: Optional[StrictBool] = Field(None, description="Bool if the metric is annualized. Default to false.")
    with_fee: Optional[StrictBool] = Field(None, alias="withFee", description="Bool if the metric should consider the fees when is calculated. Default to false.")
    seed_amount: Optional[StrictStr] = Field(None, alias="seedAmount", description="The given seed amount for the calculation of the indicative amount metrics.")
    alias: Optional[StrictStr] = Field(None, description="The alias for the metric.")
    __properties = ["type", "window", "allowPartial", "annualised", "withFee", "seedAmount", "alias"]

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
    def from_json(cls, json_str: str) -> PerformanceReturnsMetric:
        """Create an instance of PerformanceReturnsMetric from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if type (nullable) is None
        # and __fields_set__ contains the field
        if self.type is None and "type" in self.__fields_set__:
            _dict['type'] = None

        # set to None if window (nullable) is None
        # and __fields_set__ contains the field
        if self.window is None and "window" in self.__fields_set__:
            _dict['window'] = None

        # set to None if seed_amount (nullable) is None
        # and __fields_set__ contains the field
        if self.seed_amount is None and "seed_amount" in self.__fields_set__:
            _dict['seedAmount'] = None

        # set to None if alias (nullable) is None
        # and __fields_set__ contains the field
        if self.alias is None and "alias" in self.__fields_set__:
            _dict['alias'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PerformanceReturnsMetric:
        """Create an instance of PerformanceReturnsMetric from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PerformanceReturnsMetric.parse_obj(obj)

        _obj = PerformanceReturnsMetric.parse_obj({
            "type": obj.get("type"),
            "window": obj.get("window"),
            "allow_partial": obj.get("allowPartial"),
            "annualised": obj.get("annualised"),
            "with_fee": obj.get("withFee"),
            "seed_amount": obj.get("seedAmount"),
            "alias": obj.get("alias")
        })
        return _obj
