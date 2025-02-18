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


from typing import Any, Dict, Optional, Union
from pydantic.v1 import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr, constr

class CashOfferElection(BaseModel):
    """
    Election for events that result in cash via a merger or acquisition  # noqa: E501
    """
    cash_offer_currency: StrictStr = Field(..., alias="cashOfferCurrency", description="Currency of the cash offer")
    cash_offer_price: Union[StrictFloat, StrictInt] = Field(..., alias="cashOfferPrice", description="Price per share of the cash offer")
    election_key: constr(strict=True, min_length=1) = Field(..., alias="electionKey", description="Unique key associated to this election.")
    is_chosen: Optional[StrictBool] = Field(None, alias="isChosen", description="Is this the election that has been explicitly chosen from multiple options.")
    is_default: Optional[StrictBool] = Field(None, alias="isDefault", description="Is this election automatically applied in the absence of an election having been made.  May only be true for one election if multiple are provided.")
    __properties = ["cashOfferCurrency", "cashOfferPrice", "electionKey", "isChosen", "isDefault"]

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
    def from_json(cls, json_str: str) -> CashOfferElection:
        """Create an instance of CashOfferElection from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CashOfferElection:
        """Create an instance of CashOfferElection from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CashOfferElection.parse_obj(obj)

        _obj = CashOfferElection.parse_obj({
            "cash_offer_currency": obj.get("cashOfferCurrency"),
            "cash_offer_price": obj.get("cashOfferPrice"),
            "election_key": obj.get("electionKey"),
            "is_chosen": obj.get("isChosen"),
            "is_default": obj.get("isDefault")
        })
        return _obj
