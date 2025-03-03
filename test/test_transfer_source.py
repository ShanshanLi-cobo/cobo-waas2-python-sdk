# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.transfer_source import TransferSource


class TestTransferSource(unittest.TestCase):
    """TransferSource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TransferSource:
        """Test TransferSource
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TransferSource`
        """
        model = TransferSource()
        if include_optional:
            return TransferSource(
                source_type = 'Asset',
                wallet_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479',
                address = '19AR6YWEGbSoY8UT9Ksy9WrmrZPD5sL4Ku',
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
                mpc_used_key_share_holder_group = cobo_waas2.models.mpc_signing_group.MpcSigningGroup(
                    used_key_share_holder_group_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479', 
                    used_tss_node_ids = [
                        'cobo5yb7BNEBwwp5XXedbhnzQfvQtp132W4dH4Jz4x4eDp4KA'
                        ], ),
                delegate = None,
                trading_account_type = 'Asset'
            )
        else:
            return TransferSource(
                source_type = 'Asset',
                wallet_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479',
                address = '19AR6YWEGbSoY8UT9Ksy9WrmrZPD5sL4Ku',
                delegate = None,
                trading_account_type = 'Asset',
        )
        """

    def testTransferSource(self):
        """Test TransferSource"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
