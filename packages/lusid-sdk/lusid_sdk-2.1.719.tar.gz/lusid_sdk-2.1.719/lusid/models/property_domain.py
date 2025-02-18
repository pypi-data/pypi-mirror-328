# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    Contact: info@finbourne.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class PropertyDomain(str, Enum):
    """
    See https://wiki.finbourne.com/information/domain-model-properties                Each domain refers to a logical set of properties which reside within it.
    """

    """
    allowed enum values
    """
    NOTDEFINED = 'NotDefined'
    TRANSACTION = 'Transaction'
    PORTFOLIO = 'Portfolio'
    HOLDING = 'Holding'
    REFERENCEHOLDING = 'ReferenceHolding'
    TRANSACTIONCONFIGURATION = 'TransactionConfiguration'
    INSTRUMENT = 'Instrument'
    CUTLABELDEFINITION = 'CutLabelDefinition'
    ANALYTIC = 'Analytic'
    PORTFOLIOGROUP = 'PortfolioGroup'
    PERSON = 'Person'
    ACCESSMETADATA = 'AccessMetadata'
    ORDER = 'Order'
    UNITRESULT = 'UnitResult'
    MARKETDATA = 'MarketData'
    CONFIGURATIONRECIPE = 'ConfigurationRecipe'
    ALLOCATION = 'Allocation'
    CALENDAR = 'Calendar'
    LEGALENTITY = 'LegalEntity'
    PLACEMENT = 'Placement'
    EXECUTION = 'Execution'
    BLOCK = 'Block'
    PARTICIPATION = 'Participation'
    PACKAGE = 'Package'
    ORDERINSTRUCTION = 'OrderInstruction'
    NEXTBESTACTION = 'NextBestAction'
    CUSTOMENTITY = 'CustomEntity'
    INSTRUMENTEVENT = 'InstrumentEvent'
    ACCOUNT = 'Account'
    CHARTOFACCOUNTS = 'ChartOfAccounts'
    CUSTODIANACCOUNT = 'CustodianAccount'
    ABOR = 'Abor'
    ABORCONFIGURATION = 'AborConfiguration'
    FUND = 'Fund'
    FUNDCONFIGURATION = 'FundConfiguration'
    FEE = 'Fee'
    RECONCILIATION = 'Reconciliation'
    PROPERTYDEFINITION = 'PropertyDefinition'
    COMPLIANCE = 'Compliance'
    DIARYENTRY = 'DiaryEntry'
    LEG = 'Leg'
    DERIVEDVALUATION = 'DerivedValuation'
    TIMELINE = 'Timeline'
    CLOSEDPERIOD = 'ClosedPeriod'
    ADDRESSKEYDEFINITION = 'AddressKeyDefinition'
    AMORTISATIONRULESET = 'AmortisationRuleSet'
    ANALYTICSSETINVENTORY = 'AnalyticsSetInventory'
    ATOMUNITRESULT = 'AtomUnitResult'
    CLEARDOWNMODULE = 'CleardownModule'
    COMPLEXMARKETDATA = 'ComplexMarketData'
    COMPLIANCERUNSUMMARY = 'ComplianceRunSummary'
    COMPLIANCERULE = 'ComplianceRule'
    COMPLIANCERUNINFO = 'ComplianceRunInfo'
    CORPORATEACTIONSOURCE = 'CorporateActionSource'
    COUNTERPARTYAGREEMENT = 'CounterpartyAgreement'
    CUSTOMENTITYDEFINITION = 'CustomEntityDefinition'
    DATATYPE = 'DataType'
    DIALECT = 'Dialect'
    EVENTHANDLER = 'EventHandler'
    GENERALLEDGERPROFILE = 'GeneralLedgerProfile'
    POSTINGMODULE = 'PostingModule'
    QUOTE = 'Quote'
    RECIPECOMPOSER = 'RecipeComposer'
    RECONCILIATIONRUNBREAK = 'ReconciliationRunBreak'
    REFERENCELIST = 'ReferenceList'
    RELATIONDEFINITION = 'RelationDefinition'
    RETURNBLOCKINDEX = 'ReturnBlockIndex'
    SRSDOCUMENT = 'SRSDocument'
    SRSINDEX = 'SRSIndex'
    TRANSACTIONTEMPLATE = 'TransactionTemplate'
    TRANSACTIONTEMPLATESCOPE = 'TransactionTemplateScope'
    TRANSACTIONTYPE = 'TransactionType'
    TRANSACTIONTYPECONFIG = 'TransactionTypeConfig'
    TRANSLATIONSCRIPT = 'TranslationScript'
    TASKDEFINITION = 'TaskDefinition'
    TASKINSTANCE = 'TaskInstance'
    WORKER = 'Worker'
    STAGINGRULESET = 'StagingRuleSet'
    IDENTIFIERDEFINITION = 'IdentifierDefinition'

    @classmethod
    def from_json(cls, json_str: str) -> PropertyDomain:
        """Create an instance of PropertyDomain from a JSON string"""
        return PropertyDomain(json.loads(json_str))
