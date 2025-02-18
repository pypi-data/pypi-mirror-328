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
from pydantic.v1 import BaseModel, Field, conlist
from lusid.models.portfolio_return_breakdown import PortfolioReturnBreakdown

class CompositeBreakdown(BaseModel):
    """
    A list of Composite Breakdowns.  # noqa: E501
    """
    effective_at: datetime = Field(..., alias="effectiveAt", description="The effectiveAt for the calculation.")
    composite: Optional[PortfolioReturnBreakdown] = None
    constituents: Optional[conlist(PortfolioReturnBreakdown)] = Field(None, description="The constituents with their information which are part of the composite.")
    __properties = ["effectiveAt", "composite", "constituents"]

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
    def from_json(cls, json_str: str) -> CompositeBreakdown:
        """Create an instance of CompositeBreakdown from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of composite
        if self.composite:
            _dict['composite'] = self.composite.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in constituents (list)
        _items = []
        if self.constituents:
            for _item in self.constituents:
                if _item:
                    _items.append(_item.to_dict())
            _dict['constituents'] = _items
        # set to None if constituents (nullable) is None
        # and __fields_set__ contains the field
        if self.constituents is None and "constituents" in self.__fields_set__:
            _dict['constituents'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CompositeBreakdown:
        """Create an instance of CompositeBreakdown from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CompositeBreakdown.parse_obj(obj)

        _obj = CompositeBreakdown.parse_obj({
            "effective_at": obj.get("effectiveAt"),
            "composite": PortfolioReturnBreakdown.from_dict(obj.get("composite")) if obj.get("composite") is not None else None,
            "constituents": [PortfolioReturnBreakdown.from_dict(_item) for _item in obj.get("constituents")] if obj.get("constituents") is not None else None
        })
        return _obj
