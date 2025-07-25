# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.tokenization_evm_contract_call_params import TokenizationEvmContractCallParams


class TestTokenizationEvmContractCallParams(unittest.TestCase):
    """TokenizationEvmContractCallParams unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TokenizationEvmContractCallParams:
        """Test TokenizationEvmContractCallParams
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TokenizationEvmContractCallParams`
        """
        model = TokenizationEvmContractCallParams()
        if include_optional:
            return TokenizationEvmContractCallParams(
                type = 'EVM_Contract',
                calldata = '0xa22cb4650000000000000000000000001e0049783f008a0085193e00003d00cd54003c71000000000000000000000000000000000000000000000000000000000000DEMO',
                value = '1.5'
            )
        else:
            return TokenizationEvmContractCallParams(
                calldata = '0xa22cb4650000000000000000000000001e0049783f008a0085193e00003d00cd54003c71000000000000000000000000000000000000000000000000000000000000DEMO',
        )
        """

    def testTokenizationEvmContractCallParams(self):
        """Test TokenizationEvmContractCallParams"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
