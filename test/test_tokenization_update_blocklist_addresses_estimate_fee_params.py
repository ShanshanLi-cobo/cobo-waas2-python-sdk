# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.tokenization_update_blocklist_addresses_estimate_fee_params import TokenizationUpdateBlocklistAddressesEstimateFeeParams


class TestTokenizationUpdateBlocklistAddressesEstimateFeeParams(unittest.TestCase):
    """TokenizationUpdateBlocklistAddressesEstimateFeeParams unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TokenizationUpdateBlocklistAddressesEstimateFeeParams:
        """Test TokenizationUpdateBlocklistAddressesEstimateFeeParams
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TokenizationUpdateBlocklistAddressesEstimateFeeParams`
        """
        model = TokenizationUpdateBlocklistAddressesEstimateFeeParams()
        if include_optional:
            return TokenizationUpdateBlocklistAddressesEstimateFeeParams(
                action = 'Grant',
                source = None,
                addresses = [{"address":"0x789abc...","note":"reason for blocklisting"},{"address":"0xdef012..."}],
                operation_type = 'Issue',
                token_id = '8a4f9324-ef2a-43cf-9f0e-d7f99999d3e8'
            )
        else:
            return TokenizationUpdateBlocklistAddressesEstimateFeeParams(
                action = 'Grant',
                source = None,
                addresses = [{"address":"0x789abc...","note":"reason for blocklisting"},{"address":"0xdef012..."}],
                operation_type = 'Issue',
                token_id = '8a4f9324-ef2a-43cf-9f0e-d7f99999d3e8',
        )
        """

    def testTokenizationUpdateBlocklistAddressesEstimateFeeParams(self):
        """Test TokenizationUpdateBlocklistAddressesEstimateFeeParams"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
