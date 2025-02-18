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
from pydantic.v1 import BaseModel, Field, StrictBool, StrictStr

class PermIdData(BaseModel):
    """
    PermId Data Structure  # noqa: E501
    """
    figi: StrictStr = Field(..., description=">FIGI assigned to the instrument.")
    ticker: StrictStr = Field(..., description="Ticker assigned to the instrument")
    mic: StrictStr = Field(..., description="ISO market identification code(MIC) of the desired instrument(s)")
    quote_perm_id: StrictStr = Field(..., alias="quotePermId", description="QuotePermId of the instrument")
    is_primary_quote: StrictBool = Field(..., alias="isPrimaryQuote", description="If the quote is primary")
    legal_entity_identifier: Optional[StrictStr] = Field(None, alias="legalEntityIdentifier", description="LEI assigned to the instrument")
    __properties = ["figi", "ticker", "mic", "quotePermId", "isPrimaryQuote", "legalEntityIdentifier"]

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
    def from_json(cls, json_str: str) -> PermIdData:
        """Create an instance of PermIdData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if legal_entity_identifier (nullable) is None
        # and __fields_set__ contains the field
        if self.legal_entity_identifier is None and "legal_entity_identifier" in self.__fields_set__:
            _dict['legalEntityIdentifier'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PermIdData:
        """Create an instance of PermIdData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PermIdData.parse_obj(obj)

        _obj = PermIdData.parse_obj({
            "figi": obj.get("figi"),
            "ticker": obj.get("ticker"),
            "mic": obj.get("mic"),
            "quote_perm_id": obj.get("quotePermId"),
            "is_primary_quote": obj.get("isPrimaryQuote"),
            "legal_entity_identifier": obj.get("legalEntityIdentifier")
        })
        return _obj
