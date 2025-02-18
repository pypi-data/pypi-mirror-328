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
from pydantic.v1 import BaseModel, Field, constr, validator
from lusid.models.model_property import ModelProperty

class UpdateIdentifierDefinitionRequest(BaseModel):
    """
    UpdateIdentifierDefinitionRequest
    """
    hierarchy_level: Optional[constr(strict=True, max_length=512, min_length=1)] = Field(None, alias="hierarchyLevel", description="Optional metadata associated with the identifier definition.")
    display_name: Optional[constr(strict=True, max_length=256, min_length=1)] = Field(None, alias="displayName", description="A display name for the identifier. E.g. Figi.")
    description: Optional[constr(strict=True, max_length=1024, min_length=0)] = Field(None, description="An optional description for the identifier.")
    properties: Optional[Dict[str, ModelProperty]] = Field(None, description="A set of properties for the identifier definition.")
    __properties = ["hierarchyLevel", "displayName", "description", "properties"]

    @validator('hierarchy_level')
    def hierarchy_level_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[\s\S]*$", value):
            raise ValueError(r"must validate the regular expression /^[\s\S]*$/")
        return value

    @validator('display_name')
    def display_name_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[^\\<>&\"]+$", value):
            raise ValueError(r"must validate the regular expression /^[^\\<>&\"]+$/")
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
    def from_json(cls, json_str: str) -> UpdateIdentifierDefinitionRequest:
        """Create an instance of UpdateIdentifierDefinitionRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each value in properties (dict)
        _field_dict = {}
        if self.properties:
            for _key in self.properties:
                if self.properties[_key]:
                    _field_dict[_key] = self.properties[_key].to_dict()
            _dict['properties'] = _field_dict
        # set to None if hierarchy_level (nullable) is None
        # and __fields_set__ contains the field
        if self.hierarchy_level is None and "hierarchy_level" in self.__fields_set__:
            _dict['hierarchyLevel'] = None

        # set to None if display_name (nullable) is None
        # and __fields_set__ contains the field
        if self.display_name is None and "display_name" in self.__fields_set__:
            _dict['displayName'] = None

        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        # set to None if properties (nullable) is None
        # and __fields_set__ contains the field
        if self.properties is None and "properties" in self.__fields_set__:
            _dict['properties'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UpdateIdentifierDefinitionRequest:
        """Create an instance of UpdateIdentifierDefinitionRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UpdateIdentifierDefinitionRequest.parse_obj(obj)

        _obj = UpdateIdentifierDefinitionRequest.parse_obj({
            "hierarchy_level": obj.get("hierarchyLevel"),
            "display_name": obj.get("displayName"),
            "description": obj.get("description"),
            "properties": dict(
                (_k, ModelProperty.from_dict(_v))
                for _k, _v in obj.get("properties").items()
            )
            if obj.get("properties") is not None
            else None
        })
        return _obj
