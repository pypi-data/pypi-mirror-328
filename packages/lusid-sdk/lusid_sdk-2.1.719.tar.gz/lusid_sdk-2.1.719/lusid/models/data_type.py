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
from pydantic.v1 import BaseModel, Field, StrictStr, conlist, constr, validator
from lusid.models.i_unit_definition_dto import IUnitDefinitionDto
from lusid.models.link import Link
from lusid.models.reference_data import ReferenceData
from lusid.models.resource_id import ResourceId
from lusid.models.staged_modifications_info import StagedModificationsInfo
from lusid.models.version import Version

class DataType(BaseModel):
    """
    DataType
    """
    type_value_range: StrictStr = Field(..., alias="typeValueRange", description="The available values are: Open, Closed")
    id: ResourceId = Field(...)
    display_name: constr(strict=True, min_length=1) = Field(..., alias="displayName")
    description: constr(strict=True, min_length=1) = Field(...)
    value_type: StrictStr = Field(..., alias="valueType", description="The available values are: String, Int, Decimal, DateTime, Boolean, Map, List, PropertyArray, Percentage, Code, Id, Uri, CurrencyAndAmount, TradePrice, Currency, MetricValue, ResourceId, ResultValue, CutLocalTime, DateOrCutLabel, UnindexedText")
    acceptable_values: Optional[conlist(StrictStr)] = Field(None, alias="acceptableValues")
    unit_schema: Optional[StrictStr] = Field(None, alias="unitSchema", description="The available values are: NoUnits, Basic, Iso4217Currency")
    acceptable_units: Optional[conlist(IUnitDefinitionDto)] = Field(None, alias="acceptableUnits")
    reference_data: Optional[ReferenceData] = Field(None, alias="referenceData")
    version: Optional[Version] = None
    href: Optional[StrictStr] = Field(None, description="The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.")
    staged_modifications: Optional[StagedModificationsInfo] = Field(None, alias="stagedModifications")
    links: Optional[conlist(Link)] = None
    __properties = ["typeValueRange", "id", "displayName", "description", "valueType", "acceptableValues", "unitSchema", "acceptableUnits", "referenceData", "version", "href", "stagedModifications", "links"]

    @validator('type_value_range')
    def type_value_range_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('Open', 'Closed'):
            raise ValueError("must be one of enum values ('Open', 'Closed')")
        return value

    @validator('value_type')
    def value_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('String', 'Int', 'Decimal', 'DateTime', 'Boolean', 'Map', 'List', 'PropertyArray', 'Percentage', 'Code', 'Id', 'Uri', 'CurrencyAndAmount', 'TradePrice', 'Currency', 'MetricValue', 'ResourceId', 'ResultValue', 'CutLocalTime', 'DateOrCutLabel', 'UnindexedText'):
            raise ValueError("must be one of enum values ('String', 'Int', 'Decimal', 'DateTime', 'Boolean', 'Map', 'List', 'PropertyArray', 'Percentage', 'Code', 'Id', 'Uri', 'CurrencyAndAmount', 'TradePrice', 'Currency', 'MetricValue', 'ResourceId', 'ResultValue', 'CutLocalTime', 'DateOrCutLabel', 'UnindexedText')")
        return value

    @validator('unit_schema')
    def unit_schema_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('NoUnits', 'Basic', 'Iso4217Currency'):
            raise ValueError("must be one of enum values ('NoUnits', 'Basic', 'Iso4217Currency')")
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
    def from_json(cls, json_str: str) -> DataType:
        """Create an instance of DataType from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in acceptable_units (list)
        _items = []
        if self.acceptable_units:
            for _item in self.acceptable_units:
                if _item:
                    _items.append(_item.to_dict())
            _dict['acceptableUnits'] = _items
        # override the default output from pydantic by calling `to_dict()` of reference_data
        if self.reference_data:
            _dict['referenceData'] = self.reference_data.to_dict()
        # override the default output from pydantic by calling `to_dict()` of version
        if self.version:
            _dict['version'] = self.version.to_dict()
        # override the default output from pydantic by calling `to_dict()` of staged_modifications
        if self.staged_modifications:
            _dict['stagedModifications'] = self.staged_modifications.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item in self.links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['links'] = _items
        # set to None if acceptable_values (nullable) is None
        # and __fields_set__ contains the field
        if self.acceptable_values is None and "acceptable_values" in self.__fields_set__:
            _dict['acceptableValues'] = None

        # set to None if acceptable_units (nullable) is None
        # and __fields_set__ contains the field
        if self.acceptable_units is None and "acceptable_units" in self.__fields_set__:
            _dict['acceptableUnits'] = None

        # set to None if href (nullable) is None
        # and __fields_set__ contains the field
        if self.href is None and "href" in self.__fields_set__:
            _dict['href'] = None

        # set to None if links (nullable) is None
        # and __fields_set__ contains the field
        if self.links is None and "links" in self.__fields_set__:
            _dict['links'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DataType:
        """Create an instance of DataType from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DataType.parse_obj(obj)

        _obj = DataType.parse_obj({
            "type_value_range": obj.get("typeValueRange"),
            "id": ResourceId.from_dict(obj.get("id")) if obj.get("id") is not None else None,
            "display_name": obj.get("displayName"),
            "description": obj.get("description"),
            "value_type": obj.get("valueType"),
            "acceptable_values": obj.get("acceptableValues"),
            "unit_schema": obj.get("unitSchema"),
            "acceptable_units": [IUnitDefinitionDto.from_dict(_item) for _item in obj.get("acceptableUnits")] if obj.get("acceptableUnits") is not None else None,
            "reference_data": ReferenceData.from_dict(obj.get("referenceData")) if obj.get("referenceData") is not None else None,
            "version": Version.from_dict(obj.get("version")) if obj.get("version") is not None else None,
            "href": obj.get("href"),
            "staged_modifications": StagedModificationsInfo.from_dict(obj.get("stagedModifications")) if obj.get("stagedModifications") is not None else None,
            "links": [Link.from_dict(_item) for _item in obj.get("links")] if obj.get("links") is not None else None
        })
        return _obj
