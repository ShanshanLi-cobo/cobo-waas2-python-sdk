# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.tokenization_issue_estimate_fee_params import TokenizationIssueEstimateFeeParams


class TestTokenizationIssueEstimateFeeParams(unittest.TestCase):
    """TokenizationIssueEstimateFeeParams unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TokenizationIssueEstimateFeeParams:
        """Test TokenizationIssueEstimateFeeParams
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TokenizationIssueEstimateFeeParams`
        """
        model = TokenizationIssueEstimateFeeParams()
        if include_optional:
            return TokenizationIssueEstimateFeeParams(
                chain_id = 'ETH',
                source = None,
                token_params = None,
                operation_type = 'Issue'
            )
        else:
            return TokenizationIssueEstimateFeeParams(
                chain_id = 'ETH',
                source = None,
                token_params = None,
                operation_type = 'Issue',
        )
        """

    def testTokenizationIssueEstimateFeeParams(self):
        """Test TokenizationIssueEstimateFeeParams"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
