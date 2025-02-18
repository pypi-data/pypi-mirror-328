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
from lusid.models.error_detail import ErrorDetail
from lusid.models.link import Link
from lusid.models.translation_result import TranslationResult

class TranslateEntitiesResponse(BaseModel):
    """
    TranslateEntitiesResponse
    """
    values: Optional[Dict[str, TranslationResult]] = Field(None, description="The entities that were successfully translated.")
    failed: Optional[Dict[str, ErrorDetail]] = Field(None, description="The error details corresponding to entities that failed to be translated.")
    links: Optional[conlist(Link)] = None
    __properties = ["values", "failed", "links"]

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
    def from_json(cls, json_str: str) -> TranslateEntitiesResponse:
        """Create an instance of TranslateEntitiesResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each value in values (dict)
        _field_dict = {}
        if self.values:
            for _key in self.values:
                if self.values[_key]:
                    _field_dict[_key] = self.values[_key].to_dict()
            _dict['values'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each value in failed (dict)
        _field_dict = {}
        if self.failed:
            for _key in self.failed:
                if self.failed[_key]:
                    _field_dict[_key] = self.failed[_key].to_dict()
            _dict['failed'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item in self.links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['links'] = _items
        # set to None if values (nullable) is None
        # and __fields_set__ contains the field
        if self.values is None and "values" in self.__fields_set__:
            _dict['values'] = None

        # set to None if failed (nullable) is None
        # and __fields_set__ contains the field
        if self.failed is None and "failed" in self.__fields_set__:
            _dict['failed'] = None

        # set to None if links (nullable) is None
        # and __fields_set__ contains the field
        if self.links is None and "links" in self.__fields_set__:
            _dict['links'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TranslateEntitiesResponse:
        """Create an instance of TranslateEntitiesResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TranslateEntitiesResponse.parse_obj(obj)

        _obj = TranslateEntitiesResponse.parse_obj({
            "values": dict(
                (_k, TranslationResult.from_dict(_v))
                for _k, _v in obj.get("values").items()
            )
            if obj.get("values") is not None
            else None,
            "failed": dict(
                (_k, ErrorDetail.from_dict(_v))
                for _k, _v in obj.get("failed").items()
            )
            if obj.get("failed") is not None
            else None,
            "links": [Link.from_dict(_item) for _item in obj.get("links")] if obj.get("links") is not None else None
        })
        return _obj
