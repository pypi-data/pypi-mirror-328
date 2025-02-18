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
from pydantic.v1 import BaseModel, Field, constr, validator

class DataMapKey(BaseModel):
    """
    DataMapKey
    """
    version: Optional[constr(strict=True, max_length=32, min_length=0)] = Field(None, description="The version of the mappings. It is possible that a client will wish to update mappings over time. The version identifies the MAJOR.MINOR.PATCH version  of the mappings that the client assigns it.")
    code: Optional[constr(strict=True, max_length=256, min_length=1)] = Field(None, description="A unique name to semantically identify the mapping set.")
    __properties = ["version", "code"]

    @validator('version')
    def version_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^\d+\.\d+(\.\d+)?(-[a-zA-Z0-9\.-]{1,30})?$", value):
            raise ValueError(r"must validate the regular expression /^\d+\.\d+(\.\d+)?(-[a-zA-Z0-9\.-]{1,30})?$/")
        return value

    @validator('code')
    def code_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-zA-Z0-9\-_]+$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9\-_]+$/")
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
    def from_json(cls, json_str: str) -> DataMapKey:
        """Create an instance of DataMapKey from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if version (nullable) is None
        # and __fields_set__ contains the field
        if self.version is None and "version" in self.__fields_set__:
            _dict['version'] = None

        # set to None if code (nullable) is None
        # and __fields_set__ contains the field
        if self.code is None and "code" in self.__fields_set__:
            _dict['code'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DataMapKey:
        """Create an instance of DataMapKey from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DataMapKey.parse_obj(obj)

        _obj = DataMapKey.parse_obj({
            "version": obj.get("version"),
            "code": obj.get("code")
        })
        return _obj
