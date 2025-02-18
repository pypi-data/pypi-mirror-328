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
from pydantic.v1 import BaseModel, Field, conlist
from lusid.models.link import Link
from lusid.models.perpetual_property import PerpetualProperty
from lusid.models.resource_id import ResourceId
from lusid.models.version import Version

class Package(BaseModel):
    """
    A structure used to describe the structure of an order or orders that make up a non-trivial trade.  # noqa: E501
    """
    id: ResourceId = Field(...)
    order_ids: conlist(ResourceId) = Field(..., alias="orderIds", description="Related order ids.")
    order_instruction_ids: conlist(ResourceId) = Field(..., alias="orderInstructionIds", description="Related order instruction ids.")
    properties: Optional[Dict[str, PerpetualProperty]] = Field(None, description="Client-defined properties associated with this execution.")
    version: Optional[Version] = None
    links: Optional[conlist(Link)] = None
    __properties = ["id", "orderIds", "orderInstructionIds", "properties", "version", "links"]

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
    def from_json(cls, json_str: str) -> Package:
        """Create an instance of Package from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of id
        if self.id:
            _dict['id'] = self.id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in order_ids (list)
        _items = []
        if self.order_ids:
            for _item in self.order_ids:
                if _item:
                    _items.append(_item.to_dict())
            _dict['orderIds'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in order_instruction_ids (list)
        _items = []
        if self.order_instruction_ids:
            for _item in self.order_instruction_ids:
                if _item:
                    _items.append(_item.to_dict())
            _dict['orderInstructionIds'] = _items
        # override the default output from pydantic by calling `to_dict()` of each value in properties (dict)
        _field_dict = {}
        if self.properties:
            for _key in self.properties:
                if self.properties[_key]:
                    _field_dict[_key] = self.properties[_key].to_dict()
            _dict['properties'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of version
        if self.version:
            _dict['version'] = self.version.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item in self.links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['links'] = _items
        # set to None if properties (nullable) is None
        # and __fields_set__ contains the field
        if self.properties is None and "properties" in self.__fields_set__:
            _dict['properties'] = None

        # set to None if links (nullable) is None
        # and __fields_set__ contains the field
        if self.links is None and "links" in self.__fields_set__:
            _dict['links'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Package:
        """Create an instance of Package from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Package.parse_obj(obj)

        _obj = Package.parse_obj({
            "id": ResourceId.from_dict(obj.get("id")) if obj.get("id") is not None else None,
            "order_ids": [ResourceId.from_dict(_item) for _item in obj.get("orderIds")] if obj.get("orderIds") is not None else None,
            "order_instruction_ids": [ResourceId.from_dict(_item) for _item in obj.get("orderInstructionIds")] if obj.get("orderInstructionIds") is not None else None,
            "properties": dict(
                (_k, PerpetualProperty.from_dict(_v))
                for _k, _v in obj.get("properties").items()
            )
            if obj.get("properties") is not None
            else None,
            "version": Version.from_dict(obj.get("version")) if obj.get("version") is not None else None,
            "links": [Link.from_dict(_item) for _item in obj.get("links")] if obj.get("links") is not None else None
        })
        return _obj
