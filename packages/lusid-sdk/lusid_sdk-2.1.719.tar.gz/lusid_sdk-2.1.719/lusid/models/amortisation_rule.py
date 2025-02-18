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

class AmortisationRule(BaseModel):
    """
    AmortisationRule
    """
    name: constr(strict=True, max_length=256, min_length=1) = Field(..., description="The name of the rule.")
    description: Optional[constr(strict=True, max_length=1024, min_length=0)] = Field(None, description="A description of the rule.")
    filter: constr(strict=True, max_length=16384, min_length=0) = Field(..., description="The filter for this rule.")
    amortisation_method: constr(strict=True, min_length=1) = Field(..., alias="amortisationMethod", description="The filter for this rule.")
    __properties = ["name", "description", "filter", "amortisationMethod"]

    @validator('name')
    def name_validate_regular_expression(cls, value):
        """Validates the regular expression"""
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

    @validator('filter')
    def filter_validate_regular_expression(cls, value):
        """Validates the regular expression"""
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
    def from_json(cls, json_str: str) -> AmortisationRule:
        """Create an instance of AmortisationRule from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AmortisationRule:
        """Create an instance of AmortisationRule from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AmortisationRule.parse_obj(obj)

        _obj = AmortisationRule.parse_obj({
            "name": obj.get("name"),
            "description": obj.get("description"),
            "filter": obj.get("filter"),
            "amortisation_method": obj.get("amortisationMethod")
        })
        return _obj
