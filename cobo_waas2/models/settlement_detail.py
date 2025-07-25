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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from cobo_waas2.models.acquiring_type import AcquiringType
from cobo_waas2.models.bank_account import BankAccount
from cobo_waas2.models.payment_transaction import PaymentTransaction
from cobo_waas2.models.payout_channel import PayoutChannel
from cobo_waas2.models.settle_status import SettleStatus
from typing import Optional, Set
from typing_extensions import Self


class SettlementDetail(BaseModel):
    """
    SettlementDetail
    """  # noqa: E501
    currency: Optional[StrictStr] = Field(default=None, description="The fiat currency for the settlement.")
    token_id: Optional[StrictStr] = Field(default=None, description="The ID of the cryptocurrency settled.")
    chain_id: Optional[StrictStr] = Field(default=None, description="The ID of the blockchain network on which the settlement occurred.")
    merchant_id: Optional[StrictStr] = Field(default=None, description="The ID of the merchant associated with this settlement.")
    amount: Optional[StrictStr] = Field(default=None, description="The settlement amount. - If `payout_channel` is set to `Crypto`, this represents the settlement amount in the specified cryptocurrency. - If `payout_channel` is set to `OffRamp`, this represents the settlement amount in the specified fiat currency. ")
    settled_amount: Optional[StrictStr] = Field(default=None, description="The settled amount of this settlement detail.  - If `payout_channel` is set to `Crypto`, this represents the actual settled amount in the specified cryptocurrency.  - If `payout_channel` is set to `OffRamp`, this represents the actual settled amount in the specified fiat currency. ")
    status: Optional[SettleStatus] = None
    bank_account: Optional[BankAccount] = None
    transactions: Optional[List[PaymentTransaction]] = Field(default=None, description="An array of transactions associated with this settlement request. Each transaction represents a separate blockchain operation related to the settlement process.")
    created_timestamp: Optional[StrictInt] = Field(default=None, description="The creation time of the settlement, represented as a UNIX timestamp in seconds.")
    updated_timestamp: Optional[StrictInt] = Field(default=None, description="The last update time of the settlement, represented as a UNIX timestamp in seconds.")
    crypto_address_id: Optional[StrictStr] = Field(default=None, description="The ID of the crypto address used for crypto withdrawal.")
    payout_channel: Optional[PayoutChannel] = None
    acquiring_type: Optional[AcquiringType] = None
    __properties: ClassVar[List[str]] = ["currency", "token_id", "chain_id", "merchant_id", "amount", "settled_amount", "status", "bank_account", "transactions", "created_timestamp", "updated_timestamp", "crypto_address_id", "payout_channel", "acquiring_type"]

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
        """Create an instance of SettlementDetail from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of bank_account
        if self.bank_account:
            _dict['bank_account'] = self.bank_account.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in transactions (list)
        _items = []
        if self.transactions:
            for _item in self.transactions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['transactions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SettlementDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "currency": obj.get("currency"),
            "token_id": obj.get("token_id"),
            "chain_id": obj.get("chain_id"),
            "merchant_id": obj.get("merchant_id"),
            "amount": obj.get("amount"),
            "settled_amount": obj.get("settled_amount"),
            "status": obj.get("status"),
            "bank_account": BankAccount.from_dict(obj["bank_account"]) if obj.get("bank_account") is not None else None,
            "transactions": [PaymentTransaction.from_dict(_item) for _item in obj["transactions"]] if obj.get("transactions") is not None else None,
            "created_timestamp": obj.get("created_timestamp"),
            "updated_timestamp": obj.get("updated_timestamp"),
            "crypto_address_id": obj.get("crypto_address_id"),
            "payout_channel": obj.get("payout_channel"),
            "acquiring_type": obj.get("acquiring_type")
        })
        return _obj


