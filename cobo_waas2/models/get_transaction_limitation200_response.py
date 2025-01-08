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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from cobo_waas2.models.vasp import Vasp
from typing import Optional, Set
from typing_extensions import Self


class GetTransactionLimitation200Response(BaseModel):
    """
    GetTransactionLimitation200Response
    """  # noqa: E501
    vasp_list: Optional[List[Vasp]] = Field(default=None, description="A list of VASPs (Virtual Asset Service Providers) associated with the token.")
    is_threshold_reached: Optional[StrictBool] = Field(default=None, description="Indicates whether the transaction amount exceeds a predefined threshold. - **If `true`**: Additional information is required when filling Travel Rule details:   - For deposits: `date_of_incorporation` and `place_of_incorporation`. - **If `false`**: No extra fields are required. ")
    self_custody_wallet_challenge: Optional[StrictStr] = Field(default=None, description="A human-readable, time-sensitive message to be signed by the wallet owner.  The message contains key details including the wallet address, a unique nonce, and a timestamp. Signing this message confirms ownership of the wallet and allows the operation to proceed. ")
    connect_wallet_list: Optional[List[StrictStr]] = Field(default=None, description="A list of wallets connected to the system for transactions.")
    __properties: ClassVar[List[str]] = ["vasp_list", "is_threshold_reached", "self_custody_wallet_challenge", "connect_wallet_list"]

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
        """Create an instance of GetTransactionLimitation200Response from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in vasp_list (list)
        _items = []
        if self.vasp_list:
            for _item in self.vasp_list:
                if _item:
                    _items.append(_item.to_dict())
            _dict['vasp_list'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetTransactionLimitation200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "vasp_list": [Vasp.from_dict(_item) for _item in obj["vasp_list"]] if obj.get("vasp_list") is not None else None,
            "is_threshold_reached": obj.get("is_threshold_reached"),
            "self_custody_wallet_challenge": obj.get("self_custody_wallet_challenge"),
            "connect_wallet_list": obj.get("connect_wallet_list")
        })
        return _obj


