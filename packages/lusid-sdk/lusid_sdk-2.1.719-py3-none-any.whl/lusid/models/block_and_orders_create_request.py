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
from pydantic.v1 import BaseModel, Field, conlist
from lusid.models.block_and_orders_request import BlockAndOrdersRequest

class BlockAndOrdersCreateRequest(BaseModel):
    """
    BlockAndOrdersCreateRequest
    """
    requests: conlist(BlockAndOrdersRequest, max_items=100, min_items=1) = Field(..., description="A collection of BlockAndOrdersRequest.")
    __properties = ["requests"]

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
    def from_json(cls, json_str: str) -> BlockAndOrdersCreateRequest:
        """Create an instance of BlockAndOrdersCreateRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in requests (list)
        _items = []
        if self.requests:
            for _item in self.requests:
                if _item:
                    _items.append(_item.to_dict())
            _dict['requests'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BlockAndOrdersCreateRequest:
        """Create an instance of BlockAndOrdersCreateRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BlockAndOrdersCreateRequest.parse_obj(obj)

        _obj = BlockAndOrdersCreateRequest.parse_obj({
            "requests": [BlockAndOrdersRequest.from_dict(_item) for _item in obj.get("requests")] if obj.get("requests") is not None else None
        })
        return _obj
