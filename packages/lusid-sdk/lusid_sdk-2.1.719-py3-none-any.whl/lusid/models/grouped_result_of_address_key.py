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


from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist
from lusid.models.result_value import ResultValue

class GroupedResultOfAddressKey(BaseModel):
    """
    Holder class for a group of results. It consists of a list of columns and values for that column.  # noqa: E501
    """
    columns: Optional[conlist(StrictStr)] = Field(None, description="The columns, or keys, for a particular group of results")
    values: Optional[conlist(ResultValue)] = Field(None, description="The values for the list of results")
    __properties = ["columns", "values"]

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
    def from_json(cls, json_str: str) -> GroupedResultOfAddressKey:
        """Create an instance of GroupedResultOfAddressKey from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in values (list)
        _items = []
        if self.values:
            for _item in self.values:
                if _item:
                    _items.append(_item.to_dict())
            _dict['values'] = _items
        # set to None if columns (nullable) is None
        # and __fields_set__ contains the field
        if self.columns is None and "columns" in self.__fields_set__:
            _dict['columns'] = None

        # set to None if values (nullable) is None
        # and __fields_set__ contains the field
        if self.values is None and "values" in self.__fields_set__:
            _dict['values'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GroupedResultOfAddressKey:
        """Create an instance of GroupedResultOfAddressKey from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GroupedResultOfAddressKey.parse_obj(obj)

        _obj = GroupedResultOfAddressKey.parse_obj({
            "columns": obj.get("columns"),
            "values": [ResultValue.from_dict(_item) for _item in obj.get("values")] if obj.get("values") is not None else None
        })
        return _obj
