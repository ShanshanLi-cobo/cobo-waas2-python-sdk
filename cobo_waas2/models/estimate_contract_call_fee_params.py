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
from cobo_waas2.models.contract_call_destination import ContractCallDestination
from cobo_waas2.models.contract_call_source import ContractCallSource
from cobo_waas2.models.estimate_fee_request_type import EstimateFeeRequestType
from cobo_waas2.models.fee_type import FeeType
from typing import Optional, Set
from typing_extensions import Self


class EstimateContractCallFeeParams(BaseModel):
    """
    The information about a transaction that interacts with a smart contract
    """  # noqa: E501
    request_id: StrictStr = Field(description="The request ID that is used to track a transaction request. The request ID is provided by you and must be unique within your organization. It is recommended to use the same request ID as the transaction for which you want to estimate the transaction fee.")
    request_type: EstimateFeeRequestType
    chain_id: StrictStr = Field(description="The chain ID, which is the unique identifier of a blockchain. You can retrieve the IDs of all the chains you can use by calling [List enabled chains](/v2/api-references/wallets/list-enabled-chains).")
    source: ContractCallSource
    destination: ContractCallDestination
    fee_type: Optional[FeeType] = None
    __properties: ClassVar[List[str]] = ["request_id", "request_type", "chain_id", "source", "destination", "fee_type"]

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
        """Create an instance of EstimateContractCallFeeParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of source
        if self.source:
            _dict['source'] = self.source.to_dict()
        # override the default output from pydantic by calling `to_dict()` of destination
        if self.destination:
            _dict['destination'] = self.destination.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EstimateContractCallFeeParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "request_id": obj.get("request_id"),
            "request_type": obj.get("request_type"),
            "chain_id": obj.get("chain_id"),
            "source": ContractCallSource.from_dict(obj["source"]) if obj.get("source") is not None else None,
            "destination": ContractCallDestination.from_dict(obj["destination"]) if obj.get("destination") is not None else None,
            "fee_type": obj.get("fee_type")
        })
        return _obj


