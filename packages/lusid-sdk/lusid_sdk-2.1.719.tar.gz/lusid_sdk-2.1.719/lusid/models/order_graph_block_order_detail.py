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
from pydantic.v1 import BaseModel, Field, StrictStr, conlist, constr
from lusid.models.contribution_to_non_passing_rule_detail import ContributionToNonPassingRuleDetail
from lusid.models.resource_id import ResourceId

class OrderGraphBlockOrderDetail(BaseModel):
    """
    OrderGraphBlockOrderDetail
    """
    id: ResourceId = Field(...)
    compliance_state: constr(strict=True, min_length=1) = Field(..., alias="complianceState", description="The compliance state of this order. Possible values are 'Pending', 'Failed', 'Manually approved', 'Passed' and 'Warning'.")
    approval_state: constr(strict=True, min_length=1) = Field(..., alias="approvalState", description="The approval state of this order. Possible values are 'Pending', 'Rejected' and 'Approved'.")
    portfolio_id: Optional[ResourceId] = Field(None, alias="portfolioId")
    portfolio_name: Optional[StrictStr] = Field(None, alias="portfolioName", description="The name of the order's referenced Portfolio.")
    order_approval_task_id: Optional[StrictStr] = Field(None, alias="orderApprovalTaskId", description="The task id associated with the approval state of the order.")
    order_approval_task_definition_id: Optional[ResourceId] = Field(None, alias="orderApprovalTaskDefinitionId")
    non_passing_compliance_rule_results: Optional[conlist(ContributionToNonPassingRuleDetail)] = Field(None, alias="nonPassingComplianceRuleResults", description="The details of compliance rules in non-passing states.")
    __properties = ["id", "complianceState", "approvalState", "portfolioId", "portfolioName", "orderApprovalTaskId", "orderApprovalTaskDefinitionId", "nonPassingComplianceRuleResults"]

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
    def from_json(cls, json_str: str) -> OrderGraphBlockOrderDetail:
        """Create an instance of OrderGraphBlockOrderDetail from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of portfolio_id
        if self.portfolio_id:
            _dict['portfolioId'] = self.portfolio_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of order_approval_task_definition_id
        if self.order_approval_task_definition_id:
            _dict['orderApprovalTaskDefinitionId'] = self.order_approval_task_definition_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in non_passing_compliance_rule_results (list)
        _items = []
        if self.non_passing_compliance_rule_results:
            for _item in self.non_passing_compliance_rule_results:
                if _item:
                    _items.append(_item.to_dict())
            _dict['nonPassingComplianceRuleResults'] = _items
        # set to None if portfolio_name (nullable) is None
        # and __fields_set__ contains the field
        if self.portfolio_name is None and "portfolio_name" in self.__fields_set__:
            _dict['portfolioName'] = None

        # set to None if order_approval_task_id (nullable) is None
        # and __fields_set__ contains the field
        if self.order_approval_task_id is None and "order_approval_task_id" in self.__fields_set__:
            _dict['orderApprovalTaskId'] = None

        # set to None if non_passing_compliance_rule_results (nullable) is None
        # and __fields_set__ contains the field
        if self.non_passing_compliance_rule_results is None and "non_passing_compliance_rule_results" in self.__fields_set__:
            _dict['nonPassingComplianceRuleResults'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OrderGraphBlockOrderDetail:
        """Create an instance of OrderGraphBlockOrderDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OrderGraphBlockOrderDetail.parse_obj(obj)

        _obj = OrderGraphBlockOrderDetail.parse_obj({
            "id": ResourceId.from_dict(obj.get("id")) if obj.get("id") is not None else None,
            "compliance_state": obj.get("complianceState"),
            "approval_state": obj.get("approvalState"),
            "portfolio_id": ResourceId.from_dict(obj.get("portfolioId")) if obj.get("portfolioId") is not None else None,
            "portfolio_name": obj.get("portfolioName"),
            "order_approval_task_id": obj.get("orderApprovalTaskId"),
            "order_approval_task_definition_id": ResourceId.from_dict(obj.get("orderApprovalTaskDefinitionId")) if obj.get("orderApprovalTaskDefinitionId") is not None else None,
            "non_passing_compliance_rule_results": [ContributionToNonPassingRuleDetail.from_dict(_item) for _item in obj.get("nonPassingComplianceRuleResults")] if obj.get("nonPassingComplianceRuleResults") is not None else None
        })
        return _obj
