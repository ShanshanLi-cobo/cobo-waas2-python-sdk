# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.transaction_sol_fee import TransactionSOLFee


class TestTransactionSOLFee(unittest.TestCase):
    """TransactionSOLFee unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TransactionSOLFee:
        """Test TransactionSOLFee
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TransactionSOLFee`
        """
        model = TransactionSOLFee()
        if include_optional:
            return TransactionSOLFee(
                base_fee = '0.000005',
                rent_amount = '0.00001 ',
                compute_unit_price = '0.0001',
                compute_unit_limit = '200000',
                fee_type = 'EVM_EIP_1559',
                token_id = 'SOL',
                fee_used = '0.1',
                estimated_fee_used = '0.1'
            )
        else:
            return TransactionSOLFee(
                fee_type = 'EVM_EIP_1559',
        )
        """

    def testTransactionSOLFee(self):
        """Test TransactionSOLFee"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
