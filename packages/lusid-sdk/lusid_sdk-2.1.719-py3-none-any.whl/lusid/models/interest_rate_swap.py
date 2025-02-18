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
from pydantic.v1 import Field, StrictBool, StrictStr, conlist, validator
from lusid.models.additional_payment import AdditionalPayment
from lusid.models.instrument_leg import InstrumentLeg
from lusid.models.lusid_instrument import LusidInstrument

class InterestRateSwap(LusidInstrument):
    """
    LUSID representation of an Interest Rate Swap, including:      * Vanilla (single currency fixed-float non-amortising)    * CrossCurrency (>1 currency is used by the swap legs)    * Basis (single currency, floating-floating legs of different tenors)    * Amortising (the swap has 1+ leg with amortised notional)                This instrument has multiple legs, to see how legs are used in LUSID see [knowledge base article KA-02252](https://support.lusid.com/knowledgebase/article/KA-02252).                | Leg Index | Leg Identifier | Description |  | --------- | -------------- | ----------- |  | 1 | Pay/Receive | Cash flows representing the pay/receive leg. |  | 2 | Receive/Pay | Cash flows representing the receive/pay leg. |  | 3 | AdditionalPayments | Cash flows relating to any additional payments (optional). |  # noqa: E501
    """
    start_date: datetime = Field(..., alias="startDate", description="The start date of the instrument. This is normally synonymous with the trade-date.")
    maturity_date: datetime = Field(..., alias="maturityDate", description="The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.  For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as  Constant Maturity Swaps (CMS) often have sensitivities to rates that may well be observed or set prior to the maturity date, but refer to a termination date beyond it.")
    is_non_deliverable: Optional[StrictBool] = Field(None, alias="isNonDeliverable", description="Is the contract an IRS of \"Non-Deliverable\" type, meaning a single payment in the settlement currency based on the difference between  the fixed and floating rates.")
    legs: conlist(InstrumentLeg) = Field(..., description="The set of instrument legs that define the swap instrument, these should be FloatingLeg or FixedLeg.")
    settlement_ccy: Optional[StrictStr] = Field(None, alias="settlementCcy", description="Settlement currency if IRS is non-deliverable.")
    additional_payments: Optional[conlist(AdditionalPayment)] = Field(None, alias="additionalPayments", description="Optional additional payments at a given date e.g. to level off an uneven fixed-floating swap.  The dates must be distinct and either all payments are Pay or all payments are Receive.")
    instrument_type: StrictStr = Field(..., alias="instrumentType", description="The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit")
    additional_properties: Dict[str, Any] = {}
    __properties = ["instrumentType", "startDate", "maturityDate", "isNonDeliverable", "legs", "settlementCcy", "additionalPayments"]

    @validator('instrument_type')
    def instrument_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('QuotedSecurity', 'InterestRateSwap', 'FxForward', 'Future', 'ExoticInstrument', 'FxOption', 'CreditDefaultSwap', 'InterestRateSwaption', 'Bond', 'EquityOption', 'FixedLeg', 'FloatingLeg', 'BespokeCashFlowsLeg', 'Unknown', 'TermDeposit', 'ContractForDifference', 'EquitySwap', 'CashPerpetual', 'CapFloor', 'CashSettled', 'CdsIndex', 'Basket', 'FundingLeg', 'FxSwap', 'ForwardRateAgreement', 'SimpleInstrument', 'Repo', 'Equity', 'ExchangeTradedOption', 'ReferenceInstrument', 'ComplexBond', 'InflationLinkedBond', 'InflationSwap', 'SimpleCashFlowLoan', 'TotalReturnSwap', 'InflationLeg', 'FundShareClass', 'FlexibleLoan', 'UnsettledCash', 'Cash', 'MasteredInstrument', 'LoanFacility', 'FlexibleDeposit'):
            raise ValueError("must be one of enum values ('QuotedSecurity', 'InterestRateSwap', 'FxForward', 'Future', 'ExoticInstrument', 'FxOption', 'CreditDefaultSwap', 'InterestRateSwaption', 'Bond', 'EquityOption', 'FixedLeg', 'FloatingLeg', 'BespokeCashFlowsLeg', 'Unknown', 'TermDeposit', 'ContractForDifference', 'EquitySwap', 'CashPerpetual', 'CapFloor', 'CashSettled', 'CdsIndex', 'Basket', 'FundingLeg', 'FxSwap', 'ForwardRateAgreement', 'SimpleInstrument', 'Repo', 'Equity', 'ExchangeTradedOption', 'ReferenceInstrument', 'ComplexBond', 'InflationLinkedBond', 'InflationSwap', 'SimpleCashFlowLoan', 'TotalReturnSwap', 'InflationLeg', 'FundShareClass', 'FlexibleLoan', 'UnsettledCash', 'Cash', 'MasteredInstrument', 'LoanFacility', 'FlexibleDeposit')")
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
    def from_json(cls, json_str: str) -> InterestRateSwap:
        """Create an instance of InterestRateSwap from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in legs (list)
        _items = []
        if self.legs:
            for _item in self.legs:
                if _item:
                    _items.append(_item.to_dict())
            _dict['legs'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in additional_payments (list)
        _items = []
        if self.additional_payments:
            for _item in self.additional_payments:
                if _item:
                    _items.append(_item.to_dict())
            _dict['additionalPayments'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if settlement_ccy (nullable) is None
        # and __fields_set__ contains the field
        if self.settlement_ccy is None and "settlement_ccy" in self.__fields_set__:
            _dict['settlementCcy'] = None

        # set to None if additional_payments (nullable) is None
        # and __fields_set__ contains the field
        if self.additional_payments is None and "additional_payments" in self.__fields_set__:
            _dict['additionalPayments'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> InterestRateSwap:
        """Create an instance of InterestRateSwap from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return InterestRateSwap.parse_obj(obj)

        _obj = InterestRateSwap.parse_obj({
            "instrument_type": obj.get("instrumentType"),
            "start_date": obj.get("startDate"),
            "maturity_date": obj.get("maturityDate"),
            "is_non_deliverable": obj.get("isNonDeliverable"),
            "legs": [InstrumentLeg.from_dict(_item) for _item in obj.get("legs")] if obj.get("legs") is not None else None,
            "settlement_ccy": obj.get("settlementCcy"),
            "additional_payments": [AdditionalPayment.from_dict(_item) for _item in obj.get("additionalPayments")] if obj.get("additionalPayments") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
