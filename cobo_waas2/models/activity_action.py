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


class ActivityAction(str, Enum):
    """
    The specific action taken within an activity. Possible values include: - `Submitted`: Submit the staking, unstaking, or withdrawal request. - `BTCConfirmation`: The Bitcoin chain confirms the request. - `BabylonConfirmation`: The Babylon protocol confirms the request. - `DepositETH`: Deposit ETH to the validator to start staking. - `ClaimRewards`: Claim the rewards from the validator. - `ActivateValidator`: Activate the validator to start staking. - `UnstakeETH`: Unstake ETH from the validator. - `ApproveUSDC`: Grant permission for the protocol to use your USDC. - `ConvertToUSDS`: Convert your USDC to USDS. - `ApproveUSDS`: Grant permission for the protocol to use your USDS. - `DepositUSDS`: Stake the USDS with the validator. - `WithdrawUSDS`: Withdraw the USDS from the protocol. - `ConvertToUSDC`: Convert USDS back to USDC. 
    """

    """
    allowed enum values
    """
    SUBMITTED = 'Submitted'
    BTCCONFIRMATION = 'BTCConfirmation'
    BABYLONCONFIRMATION = 'BabylonConfirmation'
    DEPOSITETH = 'DepositETH'
    CLAIMREWARDS = 'ClaimRewards'
    ACTIVATEVALIDATOR = 'ActivateValidator'
    UNSTAKEETH = 'UnstakeETH'
    APPROVEUSDC = 'ApproveUSDC'
    CONVERTTOUSDS = 'ConvertToUSDS'
    APPROVEUSDS = 'ApproveUSDS'
    DEPOSITUSDS = 'DepositUSDS'
    WITHDRAWUSDS = 'WithdrawUSDS'
    CONVERTTOUSDC = 'ConvertToUSDC'

    UNKNOWN = None

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ActivityAction from a JSON string"""
        return cls(json.loads(json_str))

    @classmethod
    def _missing_(cls, value):
        return cls.UNKNOWN


