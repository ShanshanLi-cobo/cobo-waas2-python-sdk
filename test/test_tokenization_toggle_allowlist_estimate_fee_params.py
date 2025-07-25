# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.tokenization_toggle_allowlist_estimate_fee_params import TokenizationToggleAllowlistEstimateFeeParams


class TestTokenizationToggleAllowlistEstimateFeeParams(unittest.TestCase):
    """TokenizationToggleAllowlistEstimateFeeParams unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TokenizationToggleAllowlistEstimateFeeParams:
        """Test TokenizationToggleAllowlistEstimateFeeParams
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TokenizationToggleAllowlistEstimateFeeParams`
        """
        model = TokenizationToggleAllowlistEstimateFeeParams()
        if include_optional:
            return TokenizationToggleAllowlistEstimateFeeParams(
                source = None,
                activation = True,
                operation_type = 'Issue',
                token_id = '8a4f9324-ef2a-43cf-9f0e-d7f99999d3e8'
            )
        else:
            return TokenizationToggleAllowlistEstimateFeeParams(
                source = None,
                activation = True,
                operation_type = 'Issue',
                token_id = '8a4f9324-ef2a-43cf-9f0e-d7f99999d3e8',
        )
        """

    def testTokenizationToggleAllowlistEstimateFeeParams(self):
        """Test TokenizationToggleAllowlistEstimateFeeParams"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
