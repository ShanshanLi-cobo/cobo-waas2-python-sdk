# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.wallet_info import WalletInfo


class TestWalletInfo(unittest.TestCase):
    """WalletInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WalletInfo:
        """Test WalletInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WalletInfo`
        """
        model = WalletInfo()
        if include_optional:
            return WalletInfo(
                wallet_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479',
                wallet_type = 'Custodial',
                wallet_subtype = 'Asset',
                name = 'Example Wallet',
                org_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479',
                project_id = '0111039d-27fb-49ba-b172-6e0aa80e37ec',
                project_name = 'Project name',
                vault_id = '',
                vault_name = 'Vault name',
                apikey = 'd8f062da-39f4-4a11-8b9d-12595854237f',
                exchange_id = 'binance',
                main_wallet_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
            )
        else:
            return WalletInfo(
                wallet_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479',
                wallet_type = 'Custodial',
                wallet_subtype = 'Asset',
                name = 'Example Wallet',
                org_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479',
                vault_id = '',
                apikey = 'd8f062da-39f4-4a11-8b9d-12595854237f',
                exchange_id = 'binance',
        )
        """

    def testWalletInfo(self):
        """Test WalletInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
