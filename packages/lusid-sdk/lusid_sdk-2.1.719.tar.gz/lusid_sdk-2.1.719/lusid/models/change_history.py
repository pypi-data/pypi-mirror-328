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

from datetime import datetime
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist, constr, validator
from lusid.models.change_item import ChangeItem
from lusid.models.link import Link

class ChangeHistory(BaseModel):
    """
    A group of changes made by the same person at the same time.  # noqa: E501
    """
    user_id: constr(strict=True, min_length=1) = Field(..., alias="userId", description="The unique identifier of the user that made the change.")
    modified_as_at: datetime = Field(..., alias="modifiedAsAt", description="The date/time of the change.")
    request_id: constr(strict=True, min_length=1) = Field(..., alias="requestId", description="The unique identifier of the request that the changes were part of.")
    action: StrictStr = Field(..., description="The action performed on the transaction, either created, updated, or deleted. The available values are: Create, Update, Delete")
    changes: conlist(ChangeItem) = Field(..., description="The collection of changes that were made.")
    links: Optional[conlist(Link)] = None
    __properties = ["userId", "modifiedAsAt", "requestId", "action", "changes", "links"]

    @validator('action')
    def action_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('Create', 'Update', 'Delete'):
            raise ValueError("must be one of enum values ('Create', 'Update', 'Delete')")
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
    def from_json(cls, json_str: str) -> ChangeHistory:
        """Create an instance of ChangeHistory from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in changes (list)
        _items = []
        if self.changes:
            for _item in self.changes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['changes'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item in self.links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['links'] = _items
        # set to None if links (nullable) is None
        # and __fields_set__ contains the field
        if self.links is None and "links" in self.__fields_set__:
            _dict['links'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ChangeHistory:
        """Create an instance of ChangeHistory from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ChangeHistory.parse_obj(obj)

        _obj = ChangeHistory.parse_obj({
            "user_id": obj.get("userId"),
            "modified_as_at": obj.get("modifiedAsAt"),
            "request_id": obj.get("requestId"),
            "action": obj.get("action"),
            "changes": [ChangeItem.from_dict(_item) for _item in obj.get("changes")] if obj.get("changes") is not None else None,
            "links": [Link.from_dict(_item) for _item in obj.get("links")] if obj.get("links") is not None else None
        })
        return _obj
