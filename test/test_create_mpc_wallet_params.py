# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.create_mpc_wallet_params import CreateMpcWalletParams


class TestCreateMpcWalletParams(unittest.TestCase):
    """CreateMpcWalletParams unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateMpcWalletParams:
        """Test CreateMpcWalletParams
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateMpcWalletParams`
        """
        model = CreateMpcWalletParams()
        if include_optional:
            return CreateMpcWalletParams(
                name = 'My WaaS 2.0 Wallet',
                wallet_type = 'Custodial',
                wallet_subtype = 'Asset',
                vault_id = ''
            )
        else:
            return CreateMpcWalletParams(
                name = 'My WaaS 2.0 Wallet',
                wallet_type = 'Custodial',
                wallet_subtype = 'Asset',
                vault_id = '',
        )
        """

    def testCreateMpcWalletParams(self):
        """Test CreateMpcWalletParams"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
