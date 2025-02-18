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
from pydantic.v1 import BaseModel, Field, StrictStr
from lusid.models.perpetual_property import PerpetualProperty

class CancelSingleHoldingAdjustmentRequest(BaseModel):
    """
    This request specifies single target holding. i.e. holding data that the  system should match. And deletes previous adjustment made to that holding  # noqa: E501
    """
    instrument_identifiers: Dict[str, StrictStr] = Field(..., alias="instrumentIdentifiers", description="A set of instrument identifiers that can resolve the holding adjustment to a unique instrument.")
    sub_holding_keys: Optional[Dict[str, PerpetualProperty]] = Field(None, alias="subHoldingKeys", description="The sub-holding properties which identify the holding. Each property must be from the 'Transaction' domain.")
    currency: Optional[StrictStr] = Field(None, description="The Holding currency.")
    __properties = ["instrumentIdentifiers", "subHoldingKeys", "currency"]

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
    def from_json(cls, json_str: str) -> CancelSingleHoldingAdjustmentRequest:
        """Create an instance of CancelSingleHoldingAdjustmentRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each value in sub_holding_keys (dict)
        _field_dict = {}
        if self.sub_holding_keys:
            for _key in self.sub_holding_keys:
                if self.sub_holding_keys[_key]:
                    _field_dict[_key] = self.sub_holding_keys[_key].to_dict()
            _dict['subHoldingKeys'] = _field_dict
        # set to None if sub_holding_keys (nullable) is None
        # and __fields_set__ contains the field
        if self.sub_holding_keys is None and "sub_holding_keys" in self.__fields_set__:
            _dict['subHoldingKeys'] = None

        # set to None if currency (nullable) is None
        # and __fields_set__ contains the field
        if self.currency is None and "currency" in self.__fields_set__:
            _dict['currency'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CancelSingleHoldingAdjustmentRequest:
        """Create an instance of CancelSingleHoldingAdjustmentRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CancelSingleHoldingAdjustmentRequest.parse_obj(obj)

        _obj = CancelSingleHoldingAdjustmentRequest.parse_obj({
            "instrument_identifiers": obj.get("instrumentIdentifiers"),
            "sub_holding_keys": dict(
                (_k, PerpetualProperty.from_dict(_v))
                for _k, _v in obj.get("subHoldingKeys").items()
            )
            if obj.get("subHoldingKeys") is not None
            else None,
            "currency": obj.get("currency")
        })
        return _obj
