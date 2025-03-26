# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.transaction_request_utxo_fee import TransactionRequestUtxoFee


class TestTransactionRequestUtxoFee(unittest.TestCase):
    """TransactionRequestUtxoFee unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TransactionRequestUtxoFee:
        """Test TransactionRequestUtxoFee
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TransactionRequestUtxoFee`
        """
        model = TransactionRequestUtxoFee()
        if include_optional:
            return TransactionRequestUtxoFee(
                fee_rate = '50',
                fee_type = 'EVM_EIP_1559',
                token_id = 'BTC',
                max_fee_amount = '0.1'
            )
        else:
            return TransactionRequestUtxoFee(
                fee_type = 'EVM_EIP_1559',
                token_id = 'BTC',
        )
        """

    def testTransactionRequestUtxoFee(self):
        """Test TransactionRequestUtxoFee"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
