# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.contract_call_source import ContractCallSource


class TestContractCallSource(unittest.TestCase):
    """ContractCallSource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ContractCallSource:
        """Test ContractCallSource
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ContractCallSource`
        """
        model = ContractCallSource()
        if include_optional:
            return ContractCallSource(
                source_type = 'Org-Controlled',
                wallet_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479',
                address = '0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045',
                nonce = 9,
                delegate = None
            )
        else:
            return ContractCallSource(
                source_type = 'Org-Controlled',
                wallet_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479',
                address = '0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045',
                delegate = None,
        )
        """

    def testContractCallSource(self):
        """Test ContractCallSource"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
