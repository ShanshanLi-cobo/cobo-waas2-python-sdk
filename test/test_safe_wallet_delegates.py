# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.safe_wallet_delegates import SafeWalletDelegates


class TestSafeWalletDelegates(unittest.TestCase):
    """SafeWalletDelegates unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SafeWalletDelegates:
        """Test SafeWalletDelegates
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SafeWalletDelegates`
        """
        model = SafeWalletDelegates()
        if include_optional:
            return SafeWalletDelegates(
                request_type = 'Transfer',
                address = '0x1234567890123456789012345678901234567890',
                value = '1.5',
                calldata = '0xa22cb4650000000000000000000000001e0049783f008a0085193e00003d00cd54003c71000000000000000000000000000000000000000000000000000000000000DEMO',
                token_id = 'ETH',
                amount = '0.1'
            )
        else:
            return SafeWalletDelegates(
                request_type = 'Transfer',
                token_id = 'ETH',
        )
        """

    def testSafeWalletDelegates(self):
        """Test SafeWalletDelegates"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
