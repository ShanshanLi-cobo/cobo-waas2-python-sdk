# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.update_wallet_params import UpdateWalletParams


class TestUpdateWalletParams(unittest.TestCase):
    """UpdateWalletParams unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateWalletParams:
        """Test UpdateWalletParams
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateWalletParams`
        """
        model = UpdateWalletParams()
        if include_optional:
            return UpdateWalletParams(
                wallet_type = 'Custodial',
                name = 'Example Wallet'
            )
        else:
            return UpdateWalletParams(
                wallet_type = 'Custodial',
                name = 'Example Wallet',
        )
        """

    def testUpdateWalletParams(self):
        """Test UpdateWalletParams"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
