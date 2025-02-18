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
from pydantic.v1 import Field, StrictStr, constr, validator
from lusid.models.market_data_options import MarketDataOptions

class CurveOptions(MarketDataOptions):
    """
    Options for configuring how ComplexMarketData representing a 'curve' is interpreted.  # noqa: E501
    """
    day_count_convention: Optional[constr(strict=True, max_length=50, min_length=0)] = Field(None, alias="dayCountConvention", description="Day count convention of the curve. Defaults to \"Act360\".")
    front_extrapolation_type: Optional[constr(strict=True, max_length=50, min_length=0)] = Field(None, alias="frontExtrapolationType", description="What type of extrapolation is used to build the curve  Imagine that the curve is facing the observer(you), then the \"front\" direction is the closest point on the curve onward.    example: 0D tenor to past  Defaults to \"Flat\". Supported string (enumeration) values are: [None, Flat, Linear].")
    back_extrapolation_type: Optional[constr(strict=True, max_length=50, min_length=0)] = Field(None, alias="backExtrapolationType", description="What type of extrapolation is used to build the curve.    Imagine that the curve is facing the observer(you), then the \"back\" direction is the furthest point on the curve onward.  example: 30Y tenor to infinity    Defaults to \"Flat\". Supported string (enumeration) values are: [None, Flat, Linear].")
    market_data_options_type: StrictStr = Field(..., alias="marketDataOptionsType", description="The available values are: CurveOptions")
    additional_properties: Dict[str, Any] = {}
    __properties = ["marketDataOptionsType", "dayCountConvention", "frontExtrapolationType", "backExtrapolationType"]

    @validator('market_data_options_type')
    def market_data_options_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('CurveOptions'):
            raise ValueError("must be one of enum values ('CurveOptions')")
        return value

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
    def from_json(cls, json_str: str) -> CurveOptions:
        """Create an instance of CurveOptions from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if day_count_convention (nullable) is None
        # and __fields_set__ contains the field
        if self.day_count_convention is None and "day_count_convention" in self.__fields_set__:
            _dict['dayCountConvention'] = None

        # set to None if front_extrapolation_type (nullable) is None
        # and __fields_set__ contains the field
        if self.front_extrapolation_type is None and "front_extrapolation_type" in self.__fields_set__:
            _dict['frontExtrapolationType'] = None

        # set to None if back_extrapolation_type (nullable) is None
        # and __fields_set__ contains the field
        if self.back_extrapolation_type is None and "back_extrapolation_type" in self.__fields_set__:
            _dict['backExtrapolationType'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CurveOptions:
        """Create an instance of CurveOptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CurveOptions.parse_obj(obj)

        _obj = CurveOptions.parse_obj({
            "market_data_options_type": obj.get("marketDataOptionsType"),
            "day_count_convention": obj.get("dayCountConvention"),
            "front_extrapolation_type": obj.get("frontExtrapolationType"),
            "back_extrapolation_type": obj.get("backExtrapolationType")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
