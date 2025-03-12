# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from cobo_waas2.models.transaction_custodial_asset_wallet_source import TransactionCustodialAssetWalletSource
from cobo_waas2.models.transaction_deposit_from_address_source import TransactionDepositFromAddressSource
from cobo_waas2.models.transaction_deposit_from_loop_source import TransactionDepositFromLoopSource
from cobo_waas2.models.transaction_deposit_from_wallet_source import TransactionDepositFromWalletSource
from cobo_waas2.models.transaction_exchange_wallet_source import TransactionExchangeWalletSource
from cobo_waas2.models.transaction_mpc_wallet_source import TransactionMPCWalletSource
from cobo_waas2.models.transaction_smart_contract_safe_wallet_source import TransactionSmartContractSafeWalletSource
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

TRANSACTIONSOURCE_ONE_OF_SCHEMAS = ["TransactionCustodialAssetWalletSource", "TransactionDepositFromAddressSource", "TransactionDepositFromLoopSource", "TransactionDepositFromWalletSource", "TransactionExchangeWalletSource", "TransactionMPCWalletSource", "TransactionSmartContractSafeWalletSource"]

class TransactionSource(BaseModel):
    """
    TransactionSource
    """
    # data type: TransactionCustodialAssetWalletSource
    oneof_schema_1_validator: Optional[TransactionCustodialAssetWalletSource] = None
    # data type: TransactionMPCWalletSource
    oneof_schema_2_validator: Optional[TransactionMPCWalletSource] = None
    # data type: TransactionSmartContractSafeWalletSource
    oneof_schema_3_validator: Optional[TransactionSmartContractSafeWalletSource] = None
    # data type: TransactionExchangeWalletSource
    oneof_schema_4_validator: Optional[TransactionExchangeWalletSource] = None
    # data type: TransactionDepositFromAddressSource
    oneof_schema_5_validator: Optional[TransactionDepositFromAddressSource] = None
    # data type: TransactionDepositFromWalletSource
    oneof_schema_6_validator: Optional[TransactionDepositFromWalletSource] = None
    # data type: TransactionDepositFromLoopSource
    oneof_schema_7_validator: Optional[TransactionDepositFromLoopSource] = None
    actual_instance: Optional[Union[TransactionCustodialAssetWalletSource, TransactionDepositFromAddressSource, TransactionDepositFromLoopSource, TransactionDepositFromWalletSource, TransactionExchangeWalletSource, TransactionMPCWalletSource, TransactionSmartContractSafeWalletSource]] = None
    one_of_schemas: Set[str] = { "TransactionCustodialAssetWalletSource", "TransactionDepositFromAddressSource", "TransactionDepositFromLoopSource", "TransactionDepositFromWalletSource", "TransactionExchangeWalletSource", "TransactionMPCWalletSource", "TransactionSmartContractSafeWalletSource" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    discriminator_value_class_map: Dict[str, str] = {
    }

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = TransactionSource.model_construct()
        error_messages = []
        match = 0
        # validate data type: TransactionCustodialAssetWalletSource
        if not isinstance(v, TransactionCustodialAssetWalletSource):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TransactionCustodialAssetWalletSource`")
        else:
            match += 1
        # validate data type: TransactionMPCWalletSource
        if not isinstance(v, TransactionMPCWalletSource):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TransactionMPCWalletSource`")
        else:
            match += 1
        # validate data type: TransactionSmartContractSafeWalletSource
        if not isinstance(v, TransactionSmartContractSafeWalletSource):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TransactionSmartContractSafeWalletSource`")
        else:
            match += 1
        # validate data type: TransactionExchangeWalletSource
        if not isinstance(v, TransactionExchangeWalletSource):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TransactionExchangeWalletSource`")
        else:
            match += 1
        # validate data type: TransactionDepositFromAddressSource
        if not isinstance(v, TransactionDepositFromAddressSource):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TransactionDepositFromAddressSource`")
        else:
            match += 1
        # validate data type: TransactionDepositFromWalletSource
        if not isinstance(v, TransactionDepositFromWalletSource):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TransactionDepositFromWalletSource`")
        else:
            match += 1
        # validate data type: TransactionDepositFromLoopSource
        if not isinstance(v, TransactionDepositFromLoopSource):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TransactionDepositFromLoopSource`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in TransactionSource with oneOf schemas: TransactionCustodialAssetWalletSource, TransactionDepositFromAddressSource, TransactionDepositFromLoopSource, TransactionDepositFromWalletSource, TransactionExchangeWalletSource, TransactionMPCWalletSource, TransactionSmartContractSafeWalletSource. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in TransactionSource with oneOf schemas: TransactionCustodialAssetWalletSource, TransactionDepositFromAddressSource, TransactionDepositFromLoopSource, TransactionDepositFromWalletSource, TransactionExchangeWalletSource, TransactionMPCWalletSource, TransactionSmartContractSafeWalletSource. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # use oneOf discriminator to lookup the data type
        _data_type = json.loads(json_str).get("source_type")
        if not _data_type:
            raise ValueError("Failed to lookup data type from the field `source_type` in the input.")

        # check if data type is `TransactionCustodialAssetWalletSource`
        if _data_type == "Asset":
            instance.actual_instance = TransactionCustodialAssetWalletSource.from_json(json_str)
            return instance

        # check if data type is `TransactionDepositFromAddressSource`
        if _data_type == "DepositFromAddress":
            instance.actual_instance = TransactionDepositFromAddressSource.from_json(json_str)
            return instance

        # check if data type is `TransactionDepositFromLoopSource`
        if _data_type == "DepositFromLoop":
            instance.actual_instance = TransactionDepositFromLoopSource.from_json(json_str)
            return instance

        # check if data type is `TransactionDepositFromWalletSource`
        if _data_type == "DepositFromWallet":
            instance.actual_instance = TransactionDepositFromWalletSource.from_json(json_str)
            return instance

        # check if data type is `TransactionExchangeWalletSource`
        if _data_type == "Main":
            instance.actual_instance = TransactionExchangeWalletSource.from_json(json_str)
            return instance

        # check if data type is `TransactionMPCWalletSource`
        if _data_type == "Org-Controlled":
            instance.actual_instance = TransactionMPCWalletSource.from_json(json_str)
            return instance

        # check if data type is `TransactionSmartContractSafeWalletSource`
        if _data_type == "Safe{Wallet}":
            instance.actual_instance = TransactionSmartContractSafeWalletSource.from_json(json_str)
            return instance

        # check if data type is `TransactionExchangeWalletSource`
        if _data_type == "Sub":
            instance.actual_instance = TransactionExchangeWalletSource.from_json(json_str)
            return instance

        # check if data type is `TransactionMPCWalletSource`
        if _data_type == "User-Controlled":
            instance.actual_instance = TransactionMPCWalletSource.from_json(json_str)
            return instance

        # check if data type is `TransactionCustodialAssetWalletSource`
        if _data_type == "TransactionCustodialAssetWalletSource":
            instance.actual_instance = TransactionCustodialAssetWalletSource.from_json(json_str)
            return instance

        # check if data type is `TransactionDepositFromAddressSource`
        if _data_type == "TransactionDepositFromAddressSource":
            instance.actual_instance = TransactionDepositFromAddressSource.from_json(json_str)
            return instance

        # check if data type is `TransactionDepositFromLoopSource`
        if _data_type == "TransactionDepositFromLoopSource":
            instance.actual_instance = TransactionDepositFromLoopSource.from_json(json_str)
            return instance

        # check if data type is `TransactionDepositFromWalletSource`
        if _data_type == "TransactionDepositFromWalletSource":
            instance.actual_instance = TransactionDepositFromWalletSource.from_json(json_str)
            return instance

        # check if data type is `TransactionExchangeWalletSource`
        if _data_type == "TransactionExchangeWalletSource":
            instance.actual_instance = TransactionExchangeWalletSource.from_json(json_str)
            return instance

        # check if data type is `TransactionMPCWalletSource`
        if _data_type == "TransactionMPCWalletSource":
            instance.actual_instance = TransactionMPCWalletSource.from_json(json_str)
            return instance

        # check if data type is `TransactionSmartContractSafeWalletSource`
        if _data_type == "TransactionSmartContractSafeWalletSource":
            instance.actual_instance = TransactionSmartContractSafeWalletSource.from_json(json_str)
            return instance

        return instance
        # deserialize data into TransactionCustodialAssetWalletSource
        try:
            instance.actual_instance = TransactionCustodialAssetWalletSource.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into TransactionMPCWalletSource
        try:
            instance.actual_instance = TransactionMPCWalletSource.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into TransactionSmartContractSafeWalletSource
        try:
            instance.actual_instance = TransactionSmartContractSafeWalletSource.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into TransactionExchangeWalletSource
        try:
            instance.actual_instance = TransactionExchangeWalletSource.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into TransactionDepositFromAddressSource
        try:
            instance.actual_instance = TransactionDepositFromAddressSource.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into TransactionDepositFromWalletSource
        try:
            instance.actual_instance = TransactionDepositFromWalletSource.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into TransactionDepositFromLoopSource
        try:
            instance.actual_instance = TransactionDepositFromLoopSource.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into TransactionSource with oneOf schemas: TransactionCustodialAssetWalletSource, TransactionDepositFromAddressSource, TransactionDepositFromLoopSource, TransactionDepositFromWalletSource, TransactionExchangeWalletSource, TransactionMPCWalletSource, TransactionSmartContractSafeWalletSource. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            return instance
            # raise ValueError("No match found when deserializing the JSON string into TransactionSource with oneOf schemas: TransactionCustodialAssetWalletSource, TransactionDepositFromAddressSource, TransactionDepositFromLoopSource, TransactionDepositFromWalletSource, TransactionExchangeWalletSource, TransactionMPCWalletSource, TransactionSmartContractSafeWalletSource. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], TransactionCustodialAssetWalletSource, TransactionDepositFromAddressSource, TransactionDepositFromLoopSource, TransactionDepositFromWalletSource, TransactionExchangeWalletSource, TransactionMPCWalletSource, TransactionSmartContractSafeWalletSource]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


