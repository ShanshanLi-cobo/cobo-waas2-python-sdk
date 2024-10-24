# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.api_log_summary import ApiLogSummary


class TestApiLogSummary(unittest.TestCase):
    """ApiLogSummary unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiLogSummary:
        """Test ApiLogSummary
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiLogSummary`
        """
        model = ApiLogSummary()
        if include_optional:
            return ApiLogSummary(
                log_id = '924c461fae1047c3befabb50fe1633f9',
                api_method = 'GET',
                api_endpoint = '/v2/wallets/asset',
                request_timestamp = 1640918000000,
                status_code = 200
            )
        else:
            return ApiLogSummary(
                api_method = 'GET',
                api_endpoint = '/v2/wallets/asset',
                request_timestamp = 1640918000000,
                status_code = 200,
        )
        """

    def testApiLogSummary(self):
        """Test ApiLogSummary"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
