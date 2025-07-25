# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.tokenization_token_detail_info import TokenizationTokenDetailInfo


class TestTokenizationTokenDetailInfo(unittest.TestCase):
    """TokenizationTokenDetailInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TokenizationTokenDetailInfo:
        """Test TokenizationTokenDetailInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TokenizationTokenDetailInfo`
        """
        model = TokenizationTokenDetailInfo()
        if include_optional:
            return TokenizationTokenDetailInfo(
                token_id = 'ETH_CUSD2',
                chain_id = 'ETH',
                token_address = '0x1234567890123456789012345678901234567890',
                token_name = 'CUSD',
                token_symbol = 'CUSD',
                decimals = 18,
                allowlist_activated = False,
                status = 'Active',
                total_supply = '133399',
                holdings = '12399',
                permissions = [
                    cobo_waas2.models.tokenization_address_permission.TokenizationAddressPermission(
                        execution_address = '0x0406db8351aa6839169bb363f63c2c808fee8f99', 
                        permissions = ["UpgradeContract","PauseContract"], 
                        created_timestamp = 1610445878970, )
                    ]
            )
        else:
            return TokenizationTokenDetailInfo(
                token_id = 'ETH_CUSD2',
                chain_id = 'ETH',
                token_symbol = 'CUSD',
                decimals = 18,
                status = 'Active',
        )
        """

    def testTokenizationTokenDetailInfo(self):
        """Test TokenizationTokenDetailInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
