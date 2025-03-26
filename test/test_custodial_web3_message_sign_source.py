# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.custodial_web3_message_sign_source import CustodialWeb3MessageSignSource


class TestCustodialWeb3MessageSignSource(unittest.TestCase):
    """CustodialWeb3MessageSignSource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CustodialWeb3MessageSignSource:
        """Test CustodialWeb3MessageSignSource
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CustodialWeb3MessageSignSource`
        """
        model = CustodialWeb3MessageSignSource()
        if include_optional:
            return CustodialWeb3MessageSignSource(
                source_type = 'Org-Controlled',
                wallet_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479',
                address = '19AR6YWEGbSoY8UT9Ksy9WrmrZPD5sL4Ku'
            )
        else:
            return CustodialWeb3MessageSignSource(
                source_type = 'Org-Controlled',
                wallet_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479',
                address = '19AR6YWEGbSoY8UT9Ksy9WrmrZPD5sL4Ku',
        )
        """

    def testCustodialWeb3MessageSignSource(self):
        """Test CustodialWeb3MessageSignSource"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
