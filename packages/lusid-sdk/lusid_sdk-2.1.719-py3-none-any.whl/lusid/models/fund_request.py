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
from pydantic.v1 import BaseModel, Field, StrictStr, conint, conlist, constr, validator
from lusid.models.day_month import DayMonth
from lusid.models.instrument_resolution_detail import InstrumentResolutionDetail
from lusid.models.model_property import ModelProperty
from lusid.models.resource_id import ResourceId

class FundRequest(BaseModel):
    """
    The request used to create a Fund.  # noqa: E501
    """
    code: constr(strict=True, max_length=64, min_length=1) = Field(..., description="The code given for the Fund.")
    display_name: Optional[constr(strict=True, max_length=256, min_length=1)] = Field(None, alias="displayName", description="The name of the Fund.")
    description: Optional[constr(strict=True, max_length=1024, min_length=0)] = Field(None, description="A description for the Fund.")
    fund_configuration_id: ResourceId = Field(..., alias="fundConfigurationId")
    abor_id: ResourceId = Field(..., alias="aborId")
    share_class_instrument_scopes: Optional[conlist(StrictStr, max_items=1)] = Field(None, alias="shareClassInstrumentScopes", description="The scopes in which the instruments lie, currently limited to one.")
    share_class_instruments: Optional[conlist(InstrumentResolutionDetail)] = Field(None, alias="shareClassInstruments", description="Details the user-provided instrument identifiers and the instrument resolved from them.")
    type: constr(strict=True, min_length=1) = Field(..., description="The type of fund; 'Standalone', 'Master' or 'Feeder'")
    inception_date: datetime = Field(..., alias="inceptionDate", description="Inception date of the Fund")
    decimal_places: Optional[conint(strict=True, le=30, ge=0)] = Field(None, alias="decimalPlaces", description="Number of decimal places for reporting")
    year_end_date: DayMonth = Field(..., alias="yearEndDate")
    properties: Optional[Dict[str, ModelProperty]] = Field(None, description="A set of properties for the Fund.")
    __properties = ["code", "displayName", "description", "fundConfigurationId", "aborId", "shareClassInstrumentScopes", "shareClassInstruments", "type", "inceptionDate", "decimalPlaces", "yearEndDate", "properties"]

    @validator('code')
    def code_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[a-zA-Z0-9\-_]+$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9\-_]+$/")
        return value

    @validator('description')
    def description_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[\s\S]*$", value):
            raise ValueError(r"must validate the regular expression /^[\s\S]*$/")
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
    def from_json(cls, json_str: str) -> FundRequest:
        """Create an instance of FundRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of fund_configuration_id
        if self.fund_configuration_id:
            _dict['fundConfigurationId'] = self.fund_configuration_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of abor_id
        if self.abor_id:
            _dict['aborId'] = self.abor_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in share_class_instruments (list)
        _items = []
        if self.share_class_instruments:
            for _item in self.share_class_instruments:
                if _item:
                    _items.append(_item.to_dict())
            _dict['shareClassInstruments'] = _items
        # override the default output from pydantic by calling `to_dict()` of year_end_date
        if self.year_end_date:
            _dict['yearEndDate'] = self.year_end_date.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each value in properties (dict)
        _field_dict = {}
        if self.properties:
            for _key in self.properties:
                if self.properties[_key]:
                    _field_dict[_key] = self.properties[_key].to_dict()
            _dict['properties'] = _field_dict
        # set to None if display_name (nullable) is None
        # and __fields_set__ contains the field
        if self.display_name is None and "display_name" in self.__fields_set__:
            _dict['displayName'] = None

        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        # set to None if share_class_instrument_scopes (nullable) is None
        # and __fields_set__ contains the field
        if self.share_class_instrument_scopes is None and "share_class_instrument_scopes" in self.__fields_set__:
            _dict['shareClassInstrumentScopes'] = None

        # set to None if share_class_instruments (nullable) is None
        # and __fields_set__ contains the field
        if self.share_class_instruments is None and "share_class_instruments" in self.__fields_set__:
            _dict['shareClassInstruments'] = None

        # set to None if decimal_places (nullable) is None
        # and __fields_set__ contains the field
        if self.decimal_places is None and "decimal_places" in self.__fields_set__:
            _dict['decimalPlaces'] = None

        # set to None if properties (nullable) is None
        # and __fields_set__ contains the field
        if self.properties is None and "properties" in self.__fields_set__:
            _dict['properties'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> FundRequest:
        """Create an instance of FundRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FundRequest.parse_obj(obj)

        _obj = FundRequest.parse_obj({
            "code": obj.get("code"),
            "display_name": obj.get("displayName"),
            "description": obj.get("description"),
            "fund_configuration_id": ResourceId.from_dict(obj.get("fundConfigurationId")) if obj.get("fundConfigurationId") is not None else None,
            "abor_id": ResourceId.from_dict(obj.get("aborId")) if obj.get("aborId") is not None else None,
            "share_class_instrument_scopes": obj.get("shareClassInstrumentScopes"),
            "share_class_instruments": [InstrumentResolutionDetail.from_dict(_item) for _item in obj.get("shareClassInstruments")] if obj.get("shareClassInstruments") is not None else None,
            "type": obj.get("type"),
            "inception_date": obj.get("inceptionDate"),
            "decimal_places": obj.get("decimalPlaces"),
            "year_end_date": DayMonth.from_dict(obj.get("yearEndDate")) if obj.get("yearEndDate") is not None else None,
            "properties": dict(
                (_k, ModelProperty.from_dict(_v))
                for _k, _v in obj.get("properties").items()
            )
            if obj.get("properties") is not None
            else None
        })
        return _obj
