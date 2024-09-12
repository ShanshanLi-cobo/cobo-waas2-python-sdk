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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self


class TransactionTokeApproval(BaseModel):
    """
    TransactionTokeApproval
    """  # noqa: E501
    token_id: StrictStr = Field(description="The token ID, which is the unique identifier of a token. You can retrieve the IDs of all the tokens you can use by calling [List enabled tokens](/v2/api-references/wallets/list-enabled-tokens).")
    chain_id: StrictStr = Field(description="The ID of the chain on which the token operates.")
    asset_id: Optional[StrictStr] = Field(default=None, description="(This concept applies to Exchange Wallets only) The asset ID. An asset ID is the unique identifier of the asset held within your linked exchange account.")
    symbol: Optional[StrictStr] = Field(default=None, description="The token symbol, which is the abbreviated name of a token.")
    name: Optional[StrictStr] = Field(default=None, description="The token name, which is the full name of a token.")
    decimal: Optional[StrictInt] = Field(default=None, description="The token decimal.")
    icon_url: Optional[StrictStr] = Field(default=None, description="The URL of the token icon.")
    token_address: Optional[StrictStr] = Field(default=None, description="The token address, if applicable.")
    fee_token_id: Optional[StrictStr] = Field(default=None, description="The fee token ID. A fee token is the token with which you pay transaction fees.")
    can_deposit: Optional[StrictBool] = Field(default=None, description="Whether deposits are enabled for this token.")
    can_withdraw: Optional[StrictBool] = Field(default=None, description="Whether withdrawals are enabled for this token.")
    dust_threshold: Optional[StrictStr] = Field(default=None, description="The minimum withdrawal amount for Custodial Wallets. If your withdrawal amount is smaller than this threshold, the withdrawal request will receive an error.  Note: [Loop transfers](https://loop.top/) do not have this limitation. ")
    custodial_minimum_deposit_threshold: Optional[StrictStr] = Field(default=None, description="The minimum deposit amount for Custodial Wallets. If the amount you deposit to a Custodial Wallet is smaller than this threshold, the deposit will not show up on Cobo Portal or trigger any webhook events.  Note: [Loop transfers](https://loop.top/) do not have this limitation. ")
    amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Transaction value (Note that this is an absolute value. If you trade 1.5 BTC, then the value is 1.5) ")
    spender: Optional[StrictStr] = Field(default=None, description="Spender address")
    __properties: ClassVar[List[str]] = ["token_id", "chain_id", "asset_id", "symbol", "name", "decimal", "icon_url", "token_address", "fee_token_id", "can_deposit", "can_withdraw", "dust_threshold", "custodial_minimum_deposit_threshold", "amount", "spender"]

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
        """Create an instance of TransactionTokeApproval from a JSON string"""
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
        """Create an instance of TransactionTokeApproval from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "token_id": obj.get("token_id"),
            "chain_id": obj.get("chain_id"),
            "asset_id": obj.get("asset_id"),
            "symbol": obj.get("symbol"),
            "name": obj.get("name"),
            "decimal": obj.get("decimal"),
            "icon_url": obj.get("icon_url"),
            "token_address": obj.get("token_address"),
            "fee_token_id": obj.get("fee_token_id"),
            "can_deposit": obj.get("can_deposit"),
            "can_withdraw": obj.get("can_withdraw"),
            "dust_threshold": obj.get("dust_threshold"),
            "custodial_minimum_deposit_threshold": obj.get("custodial_minimum_deposit_threshold"),
            "amount": obj.get("amount"),
            "spender": obj.get("spender")
        })
        return _obj


