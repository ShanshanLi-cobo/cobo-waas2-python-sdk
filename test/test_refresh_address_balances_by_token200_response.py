# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.refresh_address_balances_by_token200_response import RefreshAddressBalancesByToken200Response


class TestRefreshAddressBalancesByToken200Response(unittest.TestCase):
    """RefreshAddressBalancesByToken200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RefreshAddressBalancesByToken200Response:
        """Test RefreshAddressBalancesByToken200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RefreshAddressBalancesByToken200Response`
        """
        model = RefreshAddressBalancesByToken200Response()
        if include_optional:
            return RefreshAddressBalancesByToken200Response(
                submitted = True
            )
        else:
            return RefreshAddressBalancesByToken200Response(
                submitted = True,
        )
        """

    def testRefreshAddressBalancesByToken200Response(self):
        """Test RefreshAddressBalancesByToken200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
