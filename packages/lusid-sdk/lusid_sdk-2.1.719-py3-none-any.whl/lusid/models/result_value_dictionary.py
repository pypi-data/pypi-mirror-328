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
from pydantic.v1 import Field, StrictStr, validator
from lusid.models.result_value import ResultValue

class ResultValueDictionary(ResultValue):
    """
    Result value for a collection of key-value pairs. Used for diagnostics associated to a cash flow, etc.  # noqa: E501
    """
    elements: Optional[Dict[str, ResultValue]] = Field(None, description="The dictionary elements")
    result_value_type: StrictStr = Field(..., alias="resultValueType", description="The available values are: ResultValue, ResultValueDictionary, ResultValue0D, ResultValueDecimal, ResultValueInt, ResultValueString, ResultValueBool, ResultValueCurrency, CashFlowValue, CashFlowValueSet, ResultValueLifeCycleEventValue, ResultValueDateTimeOffset")
    additional_properties: Dict[str, Any] = {}
    __properties = ["resultValueType", "elements"]

    @validator('result_value_type')
    def result_value_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('ResultValue', 'ResultValueDictionary', 'ResultValue0D', 'ResultValueDecimal', 'ResultValueInt', 'ResultValueString', 'ResultValueBool', 'ResultValueCurrency', 'CashFlowValue', 'CashFlowValueSet', 'ResultValueLifeCycleEventValue', 'ResultValueDateTimeOffset'):
            raise ValueError("must be one of enum values ('ResultValue', 'ResultValueDictionary', 'ResultValue0D', 'ResultValueDecimal', 'ResultValueInt', 'ResultValueString', 'ResultValueBool', 'ResultValueCurrency', 'CashFlowValue', 'CashFlowValueSet', 'ResultValueLifeCycleEventValue', 'ResultValueDateTimeOffset')")
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
    def from_json(cls, json_str: str) -> ResultValueDictionary:
        """Create an instance of ResultValueDictionary from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each value in elements (dict)
        _field_dict = {}
        if self.elements:
            for _key in self.elements:
                if self.elements[_key]:
                    _field_dict[_key] = self.elements[_key].to_dict()
            _dict['elements'] = _field_dict
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if elements (nullable) is None
        # and __fields_set__ contains the field
        if self.elements is None and "elements" in self.__fields_set__:
            _dict['elements'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ResultValueDictionary:
        """Create an instance of ResultValueDictionary from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ResultValueDictionary.parse_obj(obj)

        _obj = ResultValueDictionary.parse_obj({
            "result_value_type": obj.get("resultValueType"),
            "elements": dict(
                (_k, ResultValue.from_dict(_v))
                for _k, _v in obj.get("elements").items()
            )
            if obj.get("elements") is not None
            else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
