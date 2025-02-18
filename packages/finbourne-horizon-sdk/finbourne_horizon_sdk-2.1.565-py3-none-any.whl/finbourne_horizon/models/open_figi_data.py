# coding: utf-8

"""
    FINBOURNE Horizon API

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
from pydantic.v1 import BaseModel, Field, StrictStr

class OpenFigiData(BaseModel):
    """
    OpenFIGI data structure  # noqa: E501
    """
    figi: StrictStr = Field(..., description="FIGI assigned to the instrument.")
    name: Optional[StrictStr] = Field(None, description="Various attributes of the instrument")
    ticker: Optional[StrictStr] = Field(None, description="Various attributes of the instrument")
    exchange_code: Optional[StrictStr] = Field(None, alias="exchangeCode", description="Exchange code of the desired instrument(s)")
    mic: Optional[StrictStr] = Field(None, description="ISO market identification code(MIC) of the desired instrument(s)")
    exchange_name: Optional[StrictStr] = Field(None, alias="exchangeName", description="Exchange name of the desired instrument(s)")
    market_sector: Optional[StrictStr] = Field(None, alias="marketSector", description="Market sector description of the desired instrument(s)")
    general_security_type: Optional[StrictStr] = Field(None, alias="generalSecurityType", description="Enum-like attributes of the instrument")
    security_type: Optional[StrictStr] = Field(None, alias="securityType", description="Enum-like attributes of the instrument")
    security_description: Optional[StrictStr] = Field(None, alias="securityDescription", description="Various attributes of the instrument")
    composite_figi: Optional[StrictStr] = Field(None, alias="compositeFigi", description="Various attributes of the instrument")
    share_class_figi: Optional[StrictStr] = Field(None, alias="shareClassFigi", description="Various attributes of the instrument")
    match_type: Optional[StrictStr] = Field(None, alias="matchType", description="Type that the instrument matched against")
    search_input: Optional[StrictStr] = Field(None, alias="searchInput", description="Search input used to generate this response")
    lusid_instrument_id: Optional[StrictStr] = Field(None, alias="lusidInstrumentId", description="If an instrument with this FIGI exists, the LUID of that instrument in LUSID")
    lusid_instrument_scope: Optional[StrictStr] = Field(None, alias="lusidInstrumentScope", description="If an instrument with this FIGI exists, the Scope of that instrument in LUSID")
    __properties = ["figi", "name", "ticker", "exchangeCode", "mic", "exchangeName", "marketSector", "generalSecurityType", "securityType", "securityDescription", "compositeFigi", "shareClassFigi", "matchType", "searchInput", "lusidInstrumentId", "lusidInstrumentScope"]

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
    def from_json(cls, json_str: str) -> OpenFigiData:
        """Create an instance of OpenFigiData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if name (nullable) is None
        # and __fields_set__ contains the field
        if self.name is None and "name" in self.__fields_set__:
            _dict['name'] = None

        # set to None if ticker (nullable) is None
        # and __fields_set__ contains the field
        if self.ticker is None and "ticker" in self.__fields_set__:
            _dict['ticker'] = None

        # set to None if exchange_code (nullable) is None
        # and __fields_set__ contains the field
        if self.exchange_code is None and "exchange_code" in self.__fields_set__:
            _dict['exchangeCode'] = None

        # set to None if mic (nullable) is None
        # and __fields_set__ contains the field
        if self.mic is None and "mic" in self.__fields_set__:
            _dict['mic'] = None

        # set to None if exchange_name (nullable) is None
        # and __fields_set__ contains the field
        if self.exchange_name is None and "exchange_name" in self.__fields_set__:
            _dict['exchangeName'] = None

        # set to None if market_sector (nullable) is None
        # and __fields_set__ contains the field
        if self.market_sector is None and "market_sector" in self.__fields_set__:
            _dict['marketSector'] = None

        # set to None if general_security_type (nullable) is None
        # and __fields_set__ contains the field
        if self.general_security_type is None and "general_security_type" in self.__fields_set__:
            _dict['generalSecurityType'] = None

        # set to None if security_type (nullable) is None
        # and __fields_set__ contains the field
        if self.security_type is None and "security_type" in self.__fields_set__:
            _dict['securityType'] = None

        # set to None if security_description (nullable) is None
        # and __fields_set__ contains the field
        if self.security_description is None and "security_description" in self.__fields_set__:
            _dict['securityDescription'] = None

        # set to None if composite_figi (nullable) is None
        # and __fields_set__ contains the field
        if self.composite_figi is None and "composite_figi" in self.__fields_set__:
            _dict['compositeFigi'] = None

        # set to None if share_class_figi (nullable) is None
        # and __fields_set__ contains the field
        if self.share_class_figi is None and "share_class_figi" in self.__fields_set__:
            _dict['shareClassFigi'] = None

        # set to None if match_type (nullable) is None
        # and __fields_set__ contains the field
        if self.match_type is None and "match_type" in self.__fields_set__:
            _dict['matchType'] = None

        # set to None if search_input (nullable) is None
        # and __fields_set__ contains the field
        if self.search_input is None and "search_input" in self.__fields_set__:
            _dict['searchInput'] = None

        # set to None if lusid_instrument_id (nullable) is None
        # and __fields_set__ contains the field
        if self.lusid_instrument_id is None and "lusid_instrument_id" in self.__fields_set__:
            _dict['lusidInstrumentId'] = None

        # set to None if lusid_instrument_scope (nullable) is None
        # and __fields_set__ contains the field
        if self.lusid_instrument_scope is None and "lusid_instrument_scope" in self.__fields_set__:
            _dict['lusidInstrumentScope'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OpenFigiData:
        """Create an instance of OpenFigiData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OpenFigiData.parse_obj(obj)

        _obj = OpenFigiData.parse_obj({
            "figi": obj.get("figi"),
            "name": obj.get("name"),
            "ticker": obj.get("ticker"),
            "exchange_code": obj.get("exchangeCode"),
            "mic": obj.get("mic"),
            "exchange_name": obj.get("exchangeName"),
            "market_sector": obj.get("marketSector"),
            "general_security_type": obj.get("generalSecurityType"),
            "security_type": obj.get("securityType"),
            "security_description": obj.get("securityDescription"),
            "composite_figi": obj.get("compositeFigi"),
            "share_class_figi": obj.get("shareClassFigi"),
            "match_type": obj.get("matchType"),
            "search_input": obj.get("searchInput"),
            "lusid_instrument_id": obj.get("lusidInstrumentId"),
            "lusid_instrument_scope": obj.get("lusidInstrumentScope")
        })
        return _obj
