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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from cobo_waas2.models.smart_contract_initiator import SmartContractInitiator
from cobo_waas2.models.smart_contract_wallet_type import SmartContractWalletType
from cobo_waas2.models.wallet_subtype import WalletSubtype
from cobo_waas2.models.wallet_type import WalletType
from typing import Optional, Set
from typing_extensions import Self


class CreateSafeWalletParams(BaseModel):
    """
    CreateSafeWalletParams
    """  # noqa: E501
    name: StrictStr = Field(description="The wallet name.")
    wallet_type: WalletType
    wallet_subtype: WalletSubtype
    chain_id: StrictStr = Field(description="The ID of the chain that the wallet operates on.")
    smart_contract_wallet_type: SmartContractWalletType
    safe_address: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The address of the Smart Contract Wallet. If this is not provided, Cobo will create a new Safe{Wallet} and set up Cobo Safe for you. In that case, the `threshold` and `signers` properties are required.")
    signers: Optional[List[Annotated[str, Field(strict=True)]]] = Field(default=None, description="The signers of the Smart Contract Wallet. This property is required when creating a new Safe{Wallet}.")
    threshold: Optional[Annotated[int, Field(strict=True, ge=1)]] = Field(default=None, description="The minimum number of confirmations required for the Smart Contract Wallet. This property is required when creating a new Safe{Wallet}.")
    cobo_safe_address: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The address of Cobo Safe. If you are importing an existing Safe{Wallet}, Cobo Safe must have been created and enabled.")
    initiator: Optional[SmartContractInitiator] = None
    __properties: ClassVar[List[str]] = ["name", "wallet_type", "wallet_subtype", "chain_id", "smart_contract_wallet_type", "safe_address", "signers", "threshold", "cobo_safe_address", "initiator"]

    @field_validator('safe_address')
    def safe_address_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^0x[a-fA-F0-9]{40}$", value):
            raise ValueError(r"must validate the regular expression /^0x[a-fA-F0-9]{40}$/")
        return value

    @field_validator('cobo_safe_address')
    def cobo_safe_address_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^0x[a-fA-F0-9]{40}$", value):
            raise ValueError(r"must validate the regular expression /^0x[a-fA-F0-9]{40}$/")
        return value

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
        """Create an instance of CreateSafeWalletParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of initiator
        if self.initiator:
            _dict['initiator'] = self.initiator.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateSafeWalletParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "wallet_type": obj.get("wallet_type"),
            "wallet_subtype": obj.get("wallet_subtype"),
            "chain_id": obj.get("chain_id"),
            "smart_contract_wallet_type": obj.get("smart_contract_wallet_type"),
            "safe_address": obj.get("safe_address"),
            "signers": obj.get("signers"),
            "threshold": obj.get("threshold"),
            "cobo_safe_address": obj.get("cobo_safe_address"),
            "initiator": SmartContractInitiator.from_dict(obj["initiator"]) if obj.get("initiator") is not None else None
        })
        return _obj


