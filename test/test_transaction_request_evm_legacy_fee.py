# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.transaction_request_evm_legacy_fee import TransactionRequestEvmLegacyFee


class TestTransactionRequestEvmLegacyFee(unittest.TestCase):
    """TransactionRequestEvmLegacyFee unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TransactionRequestEvmLegacyFee:
        """Test TransactionRequestEvmLegacyFee
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TransactionRequestEvmLegacyFee`
        """
        model = TransactionRequestEvmLegacyFee()
        if include_optional:
            return TransactionRequestEvmLegacyFee(
                gas_price = '100000000',
                fee_type = 'EVM_EIP_1559',
                token_id = 'ETH',
                gas_limit = '21000'
            )
        else:
            return TransactionRequestEvmLegacyFee(
                gas_price = '100000000',
                fee_type = 'EVM_EIP_1559',
                token_id = 'ETH',
        )
        """

    def testTransactionRequestEvmLegacyFee(self):
        """Test TransactionRequestEvmLegacyFee"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
