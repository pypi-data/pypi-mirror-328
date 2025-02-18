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
from pydantic.v1 import BaseModel, Field, StrictFloat, StrictInt, StrictStr
from lusid.models.resource_id import ResourceId

class PortfolioReturnBreakdown(BaseModel):
    """
    A list of Composite Breakdowns.  # noqa: E501
    """
    portfolio_id: ResourceId = Field(..., alias="portfolioId")
    rate_of_return: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="rateOfReturn", description="The return number.")
    opening_market_value: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="openingMarketValue", description="The opening market value.")
    closing_market_value: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="closingMarketValue", description="The closing market value.")
    weight: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="The weight of the constituent into the composite.")
    constituents_in_the_composite: Optional[StrictInt] = Field(None, alias="constituentsInTheComposite", description="The number of members in the Composite on the given day.")
    constituents_missing: Optional[StrictInt] = Field(None, alias="constituentsMissing", description="The number of the constituents which have a missing return on that day.")
    currency: Optional[StrictStr] = Field(None, description="The currency of the portfolio.")
    open_fx_rate: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="openFxRate", description="The opening fxRate which is used in calculation.")
    close_fx_rate: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="closeFxRate", description="The closing fxRate which is used in calculation.")
    local_rate_of_return: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="localRateOfReturn", description="The rate of return in the local currency.")
    local_opening_market_value: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="localOpeningMarketValue", description="The opening market value in the local currency.")
    local_closing_market_value: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="localClosingMarketValue", description="The closing market value in the local currency.")
    __properties = ["portfolioId", "rateOfReturn", "openingMarketValue", "closingMarketValue", "weight", "constituentsInTheComposite", "constituentsMissing", "currency", "openFxRate", "closeFxRate", "localRateOfReturn", "localOpeningMarketValue", "localClosingMarketValue"]

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
    def from_json(cls, json_str: str) -> PortfolioReturnBreakdown:
        """Create an instance of PortfolioReturnBreakdown from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of portfolio_id
        if self.portfolio_id:
            _dict['portfolioId'] = self.portfolio_id.to_dict()
        # set to None if opening_market_value (nullable) is None
        # and __fields_set__ contains the field
        if self.opening_market_value is None and "opening_market_value" in self.__fields_set__:
            _dict['openingMarketValue'] = None

        # set to None if closing_market_value (nullable) is None
        # and __fields_set__ contains the field
        if self.closing_market_value is None and "closing_market_value" in self.__fields_set__:
            _dict['closingMarketValue'] = None

        # set to None if currency (nullable) is None
        # and __fields_set__ contains the field
        if self.currency is None and "currency" in self.__fields_set__:
            _dict['currency'] = None

        # set to None if local_rate_of_return (nullable) is None
        # and __fields_set__ contains the field
        if self.local_rate_of_return is None and "local_rate_of_return" in self.__fields_set__:
            _dict['localRateOfReturn'] = None

        # set to None if local_opening_market_value (nullable) is None
        # and __fields_set__ contains the field
        if self.local_opening_market_value is None and "local_opening_market_value" in self.__fields_set__:
            _dict['localOpeningMarketValue'] = None

        # set to None if local_closing_market_value (nullable) is None
        # and __fields_set__ contains the field
        if self.local_closing_market_value is None and "local_closing_market_value" in self.__fields_set__:
            _dict['localClosingMarketValue'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PortfolioReturnBreakdown:
        """Create an instance of PortfolioReturnBreakdown from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PortfolioReturnBreakdown.parse_obj(obj)

        _obj = PortfolioReturnBreakdown.parse_obj({
            "portfolio_id": ResourceId.from_dict(obj.get("portfolioId")) if obj.get("portfolioId") is not None else None,
            "rate_of_return": obj.get("rateOfReturn"),
            "opening_market_value": obj.get("openingMarketValue"),
            "closing_market_value": obj.get("closingMarketValue"),
            "weight": obj.get("weight"),
            "constituents_in_the_composite": obj.get("constituentsInTheComposite"),
            "constituents_missing": obj.get("constituentsMissing"),
            "currency": obj.get("currency"),
            "open_fx_rate": obj.get("openFxRate"),
            "close_fx_rate": obj.get("closeFxRate"),
            "local_rate_of_return": obj.get("localRateOfReturn"),
            "local_opening_market_value": obj.get("localOpeningMarketValue"),
            "local_closing_market_value": obj.get("localClosingMarketValue")
        })
        return _obj
