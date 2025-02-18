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
from pydantic.v1 import Field, StrictStr, conlist, validator
from lusid.models.cash_election import CashElection
from lusid.models.instrument_event import InstrumentEvent
from lusid.models.security_election import SecurityElection

class DividendOptionEvent(InstrumentEvent):
    """
    DVOP  # noqa: E501
    """
    announcement_date: Optional[datetime] = Field(None, alias="announcementDate", description="Date on which the dividend was announced / declared.")
    cash_elections: conlist(CashElection) = Field(..., alias="cashElections", description="CashElection for this DividendReinvestmentEvent")
    ex_date: datetime = Field(..., alias="exDate", description="The first business day on which the dividend is not owed to the buying party.  Typically this is T-1 from the RecordDate.")
    payment_date: datetime = Field(..., alias="paymentDate", description="The date the company pays out dividends to shareholders.")
    record_date: Optional[datetime] = Field(None, alias="recordDate", description="Date you have to be the holder of record in order to participate in the tender.")
    security_elections: conlist(SecurityElection) = Field(..., alias="securityElections", description="SecurityElection for this DividendReinvestmentEvent")
    security_settlement_date: Optional[datetime] = Field(None, alias="securitySettlementDate", description="The settlement date of the additional units.  Equal to the PaymentDate if not provided.")
    instrument_event_type: StrictStr = Field(..., alias="instrumentEventType", description="The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent")
    additional_properties: Dict[str, Any] = {}
    __properties = ["instrumentEventType", "announcementDate", "cashElections", "exDate", "paymentDate", "recordDate", "securityElections", "securitySettlementDate"]

    @validator('instrument_event_type')
    def instrument_event_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('TransitionEvent', 'InformationalEvent', 'OpenEvent', 'CloseEvent', 'StockSplitEvent', 'BondDefaultEvent', 'CashDividendEvent', 'AmortisationEvent', 'CashFlowEvent', 'ExerciseEvent', 'ResetEvent', 'TriggerEvent', 'RawVendorEvent', 'InformationalErrorEvent', 'BondCouponEvent', 'DividendReinvestmentEvent', 'AccumulationEvent', 'BondPrincipalEvent', 'DividendOptionEvent', 'MaturityEvent', 'FxForwardSettlementEvent', 'ExpiryEvent', 'ScripDividendEvent', 'StockDividendEvent', 'ReverseStockSplitEvent', 'CapitalDistributionEvent', 'SpinOffEvent', 'MergerEvent', 'FutureExpiryEvent', 'SwapCashFlowEvent', 'SwapPrincipalEvent', 'CreditPremiumCashFlowEvent', 'CdsCreditEvent', 'CdxCreditEvent', 'MbsCouponEvent', 'MbsPrincipalEvent', 'BonusIssueEvent', 'MbsPrincipalWriteOffEvent', 'MbsInterestDeferralEvent', 'MbsInterestShortfallEvent', 'TenderEvent', 'CallOnIntermediateSecuritiesEvent', 'IntermediateSecuritiesDistributionEvent', 'OptionExercisePhysicalEvent', 'OptionExerciseCashEvent', 'ProtectionPayoutCashFlowEvent', 'TermDepositInterestEvent', 'TermDepositPrincipalEvent', 'EarlyRedemptionEvent', 'FutureMarkToMarketEvent', 'AdjustGlobalCommitmentEvent', 'ContractInitialisationEvent', 'DrawdownEvent', 'LoanInterestRepaymentEvent', 'UpdateDepositAmountEvent', 'LoanPrincipalRepaymentEvent', 'DepositInterestPaymentEvent', 'DepositCloseEvent'):
            raise ValueError("must be one of enum values ('TransitionEvent', 'InformationalEvent', 'OpenEvent', 'CloseEvent', 'StockSplitEvent', 'BondDefaultEvent', 'CashDividendEvent', 'AmortisationEvent', 'CashFlowEvent', 'ExerciseEvent', 'ResetEvent', 'TriggerEvent', 'RawVendorEvent', 'InformationalErrorEvent', 'BondCouponEvent', 'DividendReinvestmentEvent', 'AccumulationEvent', 'BondPrincipalEvent', 'DividendOptionEvent', 'MaturityEvent', 'FxForwardSettlementEvent', 'ExpiryEvent', 'ScripDividendEvent', 'StockDividendEvent', 'ReverseStockSplitEvent', 'CapitalDistributionEvent', 'SpinOffEvent', 'MergerEvent', 'FutureExpiryEvent', 'SwapCashFlowEvent', 'SwapPrincipalEvent', 'CreditPremiumCashFlowEvent', 'CdsCreditEvent', 'CdxCreditEvent', 'MbsCouponEvent', 'MbsPrincipalEvent', 'BonusIssueEvent', 'MbsPrincipalWriteOffEvent', 'MbsInterestDeferralEvent', 'MbsInterestShortfallEvent', 'TenderEvent', 'CallOnIntermediateSecuritiesEvent', 'IntermediateSecuritiesDistributionEvent', 'OptionExercisePhysicalEvent', 'OptionExerciseCashEvent', 'ProtectionPayoutCashFlowEvent', 'TermDepositInterestEvent', 'TermDepositPrincipalEvent', 'EarlyRedemptionEvent', 'FutureMarkToMarketEvent', 'AdjustGlobalCommitmentEvent', 'ContractInitialisationEvent', 'DrawdownEvent', 'LoanInterestRepaymentEvent', 'UpdateDepositAmountEvent', 'LoanPrincipalRepaymentEvent', 'DepositInterestPaymentEvent', 'DepositCloseEvent')")
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
    def from_json(cls, json_str: str) -> DividendOptionEvent:
        """Create an instance of DividendOptionEvent from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in cash_elections (list)
        _items = []
        if self.cash_elections:
            for _item in self.cash_elections:
                if _item:
                    _items.append(_item.to_dict())
            _dict['cashElections'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in security_elections (list)
        _items = []
        if self.security_elections:
            for _item in self.security_elections:
                if _item:
                    _items.append(_item.to_dict())
            _dict['securityElections'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if announcement_date (nullable) is None
        # and __fields_set__ contains the field
        if self.announcement_date is None and "announcement_date" in self.__fields_set__:
            _dict['announcementDate'] = None

        # set to None if record_date (nullable) is None
        # and __fields_set__ contains the field
        if self.record_date is None and "record_date" in self.__fields_set__:
            _dict['recordDate'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DividendOptionEvent:
        """Create an instance of DividendOptionEvent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DividendOptionEvent.parse_obj(obj)

        _obj = DividendOptionEvent.parse_obj({
            "instrument_event_type": obj.get("instrumentEventType"),
            "announcement_date": obj.get("announcementDate"),
            "cash_elections": [CashElection.from_dict(_item) for _item in obj.get("cashElections")] if obj.get("cashElections") is not None else None,
            "ex_date": obj.get("exDate"),
            "payment_date": obj.get("paymentDate"),
            "record_date": obj.get("recordDate"),
            "security_elections": [SecurityElection.from_dict(_item) for _item in obj.get("securityElections")] if obj.get("securityElections") is not None else None,
            "security_settlement_date": obj.get("securitySettlementDate")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
