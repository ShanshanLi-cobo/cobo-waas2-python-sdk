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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from cobo_waas2.models.address_transfer_destination_account_output import AddressTransferDestinationAccountOutput
from cobo_waas2.models.address_transfer_destination_utxo_outputs_inner import AddressTransferDestinationUtxoOutputsInner
from cobo_waas2.models.transfer_destination_type import TransferDestinationType
from typing import Optional, Set
from typing_extensions import Self


class AddressTransferDestination(BaseModel):
    """
    The information about the transaction destination type `Address`. Refer to [Transaction sources and destinations](https://www.cobo.com/developers/v2/guides/transactions/sources-and-destinations) for a detailed introduction about the supported sources and destinations for each transaction type.  Specify either the `account_output` property or the `utxo_outputs` property. You can transfer tokens to multiple addresses only if you use MPC Wallets as the transaction source. You should use the `utxo_outputs` property to specify the destination addresses.  Switch between the tabs to display the properties for different transaction destinations. 
    """  # noqa: E501
    destination_type: TransferDestinationType
    account_output: Optional[AddressTransferDestinationAccountOutput] = None
    utxo_outputs: Optional[List[AddressTransferDestinationUtxoOutputsInner]] = None
    change_address: Optional[StrictStr] = Field(default=None, description="The address used to receive the remaining funds or change from the transaction.")
    change_output_type: Optional[StrictStr] = Field(default=None, description="The position of the change output in the transaction's outputs. Possible values are: - `Last`: The change output is placed at the end of the transaction's outputs.   - `First`: The change output is placed at the beginning of the transaction's outputs. ")
    force_internal: Optional[StrictBool] = Field(default=None, description="Whether the transaction request must be executed as a [Cobo Loop](https://manuals.cobo.com/en/portal/custodial-wallets/cobo-loop) transfer.   - `true`: The transaction request must be executed as a Cobo Loop transfer.   - `false`: The transaction request may not be executed as a Cobo Loop transfer.    Please do not set both `force_internal` and `force_external` as `true`. ")
    force_external: Optional[StrictBool] = Field(default=None, description="Whether the transaction request must not be executed as a [Cobo Loop](https://manuals.cobo.com/en/portal/custodial-wallets/cobo-loop) transfer.   - `true`: The transaction request must not be executed as a Cobo Loop transfer.   - `false`: The transaction request can be executed as a Cobo Loop transfer.  Please do not set both `force_internal` and `force_external` as `true`. ")
    __properties: ClassVar[List[str]] = ["destination_type", "account_output", "utxo_outputs", "change_address", "change_output_type", "force_internal", "force_external"]

    @field_validator('change_output_type')
    def change_output_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Last', 'First']):
            raise ValueError("must be one of enum values ('Last', 'First')")
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
        """Create an instance of AddressTransferDestination from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of account_output
        if self.account_output:
            _dict['account_output'] = self.account_output.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in utxo_outputs (list)
        _items = []
        if self.utxo_outputs:
            for _item in self.utxo_outputs:
                if _item:
                    _items.append(_item.to_dict())
            _dict['utxo_outputs'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AddressTransferDestination from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "destination_type": obj.get("destination_type"),
            "account_output": AddressTransferDestinationAccountOutput.from_dict(obj["account_output"]) if obj.get("account_output") is not None else None,
            "utxo_outputs": [AddressTransferDestinationUtxoOutputsInner.from_dict(_item) for _item in obj["utxo_outputs"]] if obj.get("utxo_outputs") is not None else None,
            "change_address": obj.get("change_address"),
            "change_output_type": obj.get("change_output_type"),
            "force_internal": obj.get("force_internal"),
            "force_external": obj.get("force_external")
        })
        return _obj


