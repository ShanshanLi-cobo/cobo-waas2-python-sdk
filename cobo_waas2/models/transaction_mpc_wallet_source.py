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
from cobo_waas2.models.transaction_source_type import TransactionSourceType
from cobo_waas2.models.transaction_utxo import TransactionUtxo
from typing import Optional, Set
from typing_extensions import Self


class TransactionMPCWalletSource(BaseModel):
    """
    Information about the transaction source type `Org-Controlled` and `User-Controlled`. 
    """  # noqa: E501
    source_type: TransactionSourceType
    wallet_id: StrictStr = Field(description="The wallet ID.")
    address: Optional[StrictStr] = Field(default=None, description="The wallet address.")
    included_utxos: Optional[List[TransactionUtxo]] = None
    excluded_utxos: Optional[List[TransactionUtxo]] = None
    signer_key_share_holder_group_id: Optional[StrictStr] = Field(default=None, description="The ID of the key share holder group that is selected to sign the transaction.")
    __properties: ClassVar[List[str]] = ["source_type", "wallet_id", "address", "included_utxos", "excluded_utxos", "signer_key_share_holder_group_id"]

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
        """Create an instance of TransactionMPCWalletSource from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in included_utxos (list)
        _items = []
        if self.included_utxos:
            for _item in self.included_utxos:
                if _item:
                    _items.append(_item.to_dict())
            _dict['included_utxos'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in excluded_utxos (list)
        _items = []
        if self.excluded_utxos:
            for _item in self.excluded_utxos:
                if _item:
                    _items.append(_item.to_dict())
            _dict['excluded_utxos'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TransactionMPCWalletSource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "source_type": obj.get("source_type"),
            "wallet_id": obj.get("wallet_id"),
            "address": obj.get("address"),
            "included_utxos": [TransactionUtxo.from_dict(_item) for _item in obj["included_utxos"]] if obj.get("included_utxos") is not None else None,
            "excluded_utxos": [TransactionUtxo.from_dict(_item) for _item in obj["excluded_utxos"]] if obj.get("excluded_utxos") is not None else None,
            "signer_key_share_holder_group_id": obj.get("signer_key_share_holder_group_id")
        })
        return _obj


