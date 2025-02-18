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
from typing import Any, Dict, List, Optional, Union
from pydantic.v1 import BaseModel, Field, StrictFloat, StrictInt, StrictStr, conlist
from lusid.models.currency_and_amount import CurrencyAndAmount
from lusid.models.link import Link
from lusid.models.perpetual_property import PerpetualProperty
from lusid.models.resource_id import ResourceId
from lusid.models.version import Version

class OrderInstruction(BaseModel):
    """
    Record of an order instruction  # noqa: E501
    """
    id: ResourceId = Field(...)
    created_date: datetime = Field(..., alias="createdDate", description="The active date of this order instruction.")
    properties: Optional[Dict[str, PerpetualProperty]] = Field(None, description="Client-defined properties associated with this execution.")
    portfolio_id: Optional[ResourceId] = Field(None, alias="portfolioId")
    instrument_identifiers: Dict[str, StrictStr] = Field(..., alias="instrumentIdentifiers", description="The instrument ordered.")
    quantity: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="The quantity of given instrument ordered.")
    weight: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="The weight of given instrument ordered.")
    price: Optional[CurrencyAndAmount] = None
    instrument_scope: Optional[StrictStr] = Field(None, alias="instrumentScope", description="The scope in which the instrument lies")
    lusid_instrument_id: Optional[StrictStr] = Field(None, alias="lusidInstrumentId", description="The LUSID instrument id for the instrument ordered.")
    version: Optional[Version] = None
    links: Optional[conlist(Link)] = None
    __properties = ["id", "createdDate", "properties", "portfolioId", "instrumentIdentifiers", "quantity", "weight", "price", "instrumentScope", "lusidInstrumentId", "version", "links"]

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
    def from_json(cls, json_str: str) -> OrderInstruction:
        """Create an instance of OrderInstruction from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each value in properties (dict)
        _field_dict = {}
        if self.properties:
            for _key in self.properties:
                if self.properties[_key]:
                    _field_dict[_key] = self.properties[_key].to_dict()
            _dict['properties'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of portfolio_id
        if self.portfolio_id:
            _dict['portfolioId'] = self.portfolio_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of price
        if self.price:
            _dict['price'] = self.price.to_dict()
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

        # set to None if quantity (nullable) is None
        # and __fields_set__ contains the field
        if self.quantity is None and "quantity" in self.__fields_set__:
            _dict['quantity'] = None

        # set to None if weight (nullable) is None
        # and __fields_set__ contains the field
        if self.weight is None and "weight" in self.__fields_set__:
            _dict['weight'] = None

        # set to None if instrument_scope (nullable) is None
        # and __fields_set__ contains the field
        if self.instrument_scope is None and "instrument_scope" in self.__fields_set__:
            _dict['instrumentScope'] = None

        # set to None if lusid_instrument_id (nullable) is None
        # and __fields_set__ contains the field
        if self.lusid_instrument_id is None and "lusid_instrument_id" in self.__fields_set__:
            _dict['lusidInstrumentId'] = None

        # set to None if links (nullable) is None
        # and __fields_set__ contains the field
        if self.links is None and "links" in self.__fields_set__:
            _dict['links'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OrderInstruction:
        """Create an instance of OrderInstruction from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OrderInstruction.parse_obj(obj)

        _obj = OrderInstruction.parse_obj({
            "id": ResourceId.from_dict(obj.get("id")) if obj.get("id") is not None else None,
            "created_date": obj.get("createdDate"),
            "properties": dict(
                (_k, PerpetualProperty.from_dict(_v))
                for _k, _v in obj.get("properties").items()
            )
            if obj.get("properties") is not None
            else None,
            "portfolio_id": ResourceId.from_dict(obj.get("portfolioId")) if obj.get("portfolioId") is not None else None,
            "instrument_identifiers": obj.get("instrumentIdentifiers"),
            "quantity": obj.get("quantity"),
            "weight": obj.get("weight"),
            "price": CurrencyAndAmount.from_dict(obj.get("price")) if obj.get("price") is not None else None,
            "instrument_scope": obj.get("instrumentScope"),
            "lusid_instrument_id": obj.get("lusidInstrumentId"),
            "version": Version.from_dict(obj.get("version")) if obj.get("version") is not None else None,
            "links": [Link.from_dict(_item) for _item in obj.get("links")] if obj.get("links") is not None else None
        })
        return _obj
