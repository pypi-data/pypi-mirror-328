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
from pydantic.v1 import BaseModel, Field, StrictStr, constr

class TransactionPropertyMap(BaseModel):
    """
    TransactionPropertyMap
    """
    property_key: Optional[StrictStr] = Field(None, alias="propertyKey", description="The key that uniquely identifies the property. It has the format {domain}/{scope}/{code}.")
    value: Optional[constr(strict=True, max_length=1024, min_length=0)] = None
    __properties = ["propertyKey", "value"]

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
    def from_json(cls, json_str: str) -> TransactionPropertyMap:
        """Create an instance of TransactionPropertyMap from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if property_key (nullable) is None
        # and __fields_set__ contains the field
        if self.property_key is None and "property_key" in self.__fields_set__:
            _dict['propertyKey'] = None

        # set to None if value (nullable) is None
        # and __fields_set__ contains the field
        if self.value is None and "value" in self.__fields_set__:
            _dict['value'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TransactionPropertyMap:
        """Create an instance of TransactionPropertyMap from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TransactionPropertyMap.parse_obj(obj)

        _obj = TransactionPropertyMap.parse_obj({
            "property_key": obj.get("propertyKey"),
            "value": obj.get("value")
        })
        return _obj
