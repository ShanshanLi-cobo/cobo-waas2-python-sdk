# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: support@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.mpc_wallet_info import MPCWalletInfo


class TestMPCWalletInfo(unittest.TestCase):
    """MPCWalletInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MPCWalletInfo:
        """Test MPCWalletInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MPCWalletInfo`
        """
        model = MPCWalletInfo()
        if include_optional:
            return MPCWalletInfo(
                wallet_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479',
                wallet_type = 'Custodial',
                wallet_subtype = 'Asset',
                name = 'Example Wallet',
                org_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479',
                project_id = '0111039d-27fb-49ba-b172-6e0aa80e37ec',
                project_name = 'Project name',
                vault_id = '',
                vault_name = 'Vault name'
            )
        else:
            return MPCWalletInfo(
                wallet_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479',
                wallet_type = 'Custodial',
                wallet_subtype = 'Asset',
                name = 'Example Wallet',
                org_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479',
                vault_id = '',
        )
        """

    def testMPCWalletInfo(self):
        """Test MPCWalletInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
