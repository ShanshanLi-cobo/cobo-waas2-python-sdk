# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.get_token4_xx_response import GetToken4XXResponse


class TestGetToken4XXResponse(unittest.TestCase):
    """GetToken4XXResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetToken4XXResponse:
        """Test GetToken4XXResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetToken4XXResponse`
        """
        model = GetToken4XXResponse()
        if include_optional:
            return GetToken4XXResponse(
                error = '',
                error_message = ''
            )
        else:
            return GetToken4XXResponse(
                error = '',
        )
        """

    def testGetToken4XXResponse(self):
        """Test GetToken4XXResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
