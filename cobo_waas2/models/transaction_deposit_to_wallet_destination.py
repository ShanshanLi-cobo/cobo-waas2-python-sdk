# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: support@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from cobo_waas2.models.exchange_id import ExchangeId
from cobo_waas2.models.transaction_destination_type import TransactionDestinationType
from cobo_waas2.models.wallet_subtype import WalletSubtype
from cobo_waas2.models.wallet_type import WalletType
from typing import Optional, Set
from typing_extensions import Self


class TransactionDepositToWalletDestination(BaseModel):
    """
    Information about the transaction destination type `DepositToWallet`. 
    """  # noqa: E501
    destination_type: TransactionDestinationType
    wallet_id: StrictStr = Field(description="The wallet ID.")
    wallet_type: WalletType
    wallet_subtype: WalletSubtype
    trading_account_type: Optional[StrictStr] = Field(default=None, description="The trading account type.")
    exchange_id: Optional[ExchangeId] = None
    amount: StrictStr = Field(description="The transfer amount. For example, if you trade 1.5 ETH, then the value is `1.5`. ")
    __properties: ClassVar[List[str]] = ["destination_type", "wallet_id", "wallet_type", "wallet_subtype", "trading_account_type", "exchange_id", "amount"]

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
        """Create an instance of TransactionDepositToWalletDestination from a JSON string"""
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
        """Create an instance of TransactionDepositToWalletDestination from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "destination_type": obj.get("destination_type"),
            "wallet_id": obj.get("wallet_id"),
            "wallet_type": obj.get("wallet_type"),
            "wallet_subtype": obj.get("wallet_subtype"),
            "trading_account_type": obj.get("trading_account_type"),
            "exchange_id": obj.get("exchange_id"),
            "amount": obj.get("amount")
        })
        return _obj


