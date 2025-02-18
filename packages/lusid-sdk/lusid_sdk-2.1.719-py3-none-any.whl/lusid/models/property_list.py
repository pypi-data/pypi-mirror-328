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


from typing import Any, Dict, List
from pydantic.v1 import Field, StrictStr, conlist, validator
from lusid.models.model_property import ModelProperty
from lusid.models.reference_list import ReferenceList

class PropertyList(ReferenceList):
    """
    PropertyList
    """
    values: conlist(ModelProperty, max_items=10000, min_items=0) = Field(...)
    reference_list_type: StrictStr = Field(..., alias="referenceListType", description="The reference list values. The available values are: PortfolioGroupIdList, PortfolioIdList, AddressKeyList, StringList, InstrumentList, DecimalList, PropertyList, FundIdList")
    additional_properties: Dict[str, Any] = {}
    __properties = ["referenceListType", "values"]

    @validator('reference_list_type')
    def reference_list_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('PortfolioGroupIdList', 'PortfolioIdList', 'AddressKeyList', 'StringList', 'InstrumentList', 'DecimalList', 'PropertyList', 'FundIdList'):
            raise ValueError("must be one of enum values ('PortfolioGroupIdList', 'PortfolioIdList', 'AddressKeyList', 'StringList', 'InstrumentList', 'DecimalList', 'PropertyList', 'FundIdList')")
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
    def from_json(cls, json_str: str) -> PropertyList:
        """Create an instance of PropertyList from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in values (list)
        _items = []
        if self.values:
            for _item in self.values:
                if _item:
                    _items.append(_item.to_dict())
            _dict['values'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PropertyList:
        """Create an instance of PropertyList from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PropertyList.parse_obj(obj)

        _obj = PropertyList.parse_obj({
            "reference_list_type": obj.get("referenceListType"),
            "values": [ModelProperty.from_dict(_item) for _item in obj.get("values")] if obj.get("values") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
