# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.transaction_source import TransactionSource


class TestTransactionSource(unittest.TestCase):
    """TransactionSource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TransactionSource:
        """Test TransactionSource
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TransactionSource`
        """
        model = TransactionSource()
        if include_optional:
            return TransactionSource(
                source_type = 'DepositFromAddress',
                wallet_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479',
                address = '0x1234567890123456789012345678901234567890',
                included_utxos = [
                    cobo_waas2.models.transaction_utxo.TransactionUtxo(
                        tx_hash = '7014d7d9b91862d7131f7543d84da3bec60e20be93c23ad01167c48b778fdemo', 
                        vout_n = 0, )
                    ],
                excluded_utxos = [
                    cobo_waas2.models.transaction_utxo.TransactionUtxo(
                        tx_hash = '7014d7d9b91862d7131f7543d84da3bec60e20be93c23ad01167c48b778fdemo', 
                        vout_n = 0, )
                    ],
                signer_key_share_holder_group_id = 'b33130a9-6e18-44a9-9e48-8b3b41921f0e',
                delegate = None,
                exchange_id = 'binance',
                trading_account_type = 'Asset',
                wallet_type = 'Custodial',
                wallet_subtype = 'Asset',
                addresses = [
                    '19AR6YWEGbSoY8UT9Ksy9WrmrZPD5sL4Ku'
                    ]
            )
        else:
            return TransactionSource(
                source_type = 'DepositFromAddress',
                wallet_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479',
                address = '0x1234567890123456789012345678901234567890',
                exchange_id = 'binance',
                wallet_type = 'Custodial',
                wallet_subtype = 'Asset',
                addresses = [
                    '19AR6YWEGbSoY8UT9Ksy9WrmrZPD5sL4Ku'
                    ],
        )
        """

    def testTransactionSource(self):
        """Test TransactionSource"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
