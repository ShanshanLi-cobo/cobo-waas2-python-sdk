# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from cobo_waas2.models.fee_type import FeeType
from typing import Optional, Set
from typing_extensions import Self


class TransactionFixedFee(BaseModel):
    """
    The transaction fee actually charged by the chain that uses the fixed fee model.   Switch between the tabs to display the properties for different transaction fee models. 
    """  # noqa: E501
    max_fee_amount: Optional[StrictStr] = Field(default=None, description="The maximum fee that you are willing to pay for the transaction. Provide the value without applying precision. The transaction will fail if the transaction fee exceeds the maximum fee.")
    fee_type: FeeType
    token_id: Optional[StrictStr] = Field(default=None, description="The token used to pay the transaction fee.")
    fee_used: Optional[StrictStr] = Field(default=None, description="The actually charged transaction fee.")
    estimated_fee_used: Optional[StrictStr] = Field(default=None, description="The estimated transaction fee.")
    __properties: ClassVar[List[str]] = ["max_fee_amount", "fee_type", "token_id", "fee_used", "estimated_fee_used"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of TransactionFixedFee from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TransactionFixedFee from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "max_fee_amount": obj.get("max_fee_amount"),
            "fee_type": obj.get("fee_type"),
            "token_id": obj.get("token_id"),
            "fee_used": obj.get("fee_used"),
            "estimated_fee_used": obj.get("estimated_fee_used")
        })
        return _obj


