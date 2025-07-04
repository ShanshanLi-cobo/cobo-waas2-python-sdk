# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.transaction_request_fil_fee import TransactionRequestFILFee


class TestTransactionRequestFILFee(unittest.TestCase):
    """TransactionRequestFILFee unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TransactionRequestFILFee:
        """Test TransactionRequestFILFee
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TransactionRequestFILFee`
        """
        model = TransactionRequestFILFee()
        if include_optional:
            return TransactionRequestFILFee(
                gas_premium = '0.0001',
                gas_fee_cap = '0.00035',
                gas_limit = '500',
                fee_type = 'EVM_EIP_1559',
                token_id = 'ETH'
            )
        else:
            return TransactionRequestFILFee(
                gas_premium = '0.0001',
                gas_fee_cap = '0.00035',
                fee_type = 'EVM_EIP_1559',
                token_id = 'ETH',
        )
        """

    def testTransactionRequestFILFee(self):
        """Test TransactionRequestFILFee"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
