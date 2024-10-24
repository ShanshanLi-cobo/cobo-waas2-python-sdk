# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class WalletSubtype(str, Enum):
    """
    The wallet sub-type. Possible values include: - `Asset`: Custodial Wallets (Asset Wallets). - `Org-Controlled`: MPC Wallets (Organization-Controlled Wallets). - `User-Controlled`: MPC Wallets (User-Controlled Wallets). - `Safe{Wallet}`: Smart Contract Wallets (Safe). - `Main`: Exchange Wallets (Main Account). - `Sub`: Exchange Wallets (Sub Account).  Each wallet sub-type requires a different set of properties. Switch between the above tabs for details. 
    """

    """
    allowed enum values
    """
    ASSET = 'Asset'
    WEB3 = 'Web3'
    ORG_CONTROLLED = 'Org-Controlled'
    USER_CONTROLLED = 'User-Controlled'
    SAFE_WALLET = 'Safe{Wallet}'
    MAIN = 'Main'
    SUB = 'Sub'

    UNKNOWN = None

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of WalletSubtype from a JSON string"""
        return cls(json.loads(json_str))

    @classmethod
    def _missing_(cls, value):
        return cls.UNKNOWN


