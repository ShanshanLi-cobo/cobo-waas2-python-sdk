# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.create_approval_request201_response import CreateApprovalRequest201Response


class TestCreateApprovalRequest201Response(unittest.TestCase):
    """CreateApprovalRequest201Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateApprovalRequest201Response:
        """Test CreateApprovalRequest201Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateApprovalRequest201Response`
        """
        model = CreateApprovalRequest201Response()
        if include_optional:
            return CreateApprovalRequest201Response(
                approval_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
            )
        else:
            return CreateApprovalRequest201Response(
                approval_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479',
        )
        """

    def testCreateApprovalRequest201Response(self):
        """Test CreateApprovalRequest201Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
