# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: support@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.check_loop_transfers200_response_inner import CheckLoopTransfers200ResponseInner


class TestCheckLoopTransfers200ResponseInner(unittest.TestCase):
    """CheckLoopTransfers200ResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CheckLoopTransfers200ResponseInner:
        """Test CheckLoopTransfers200ResponseInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CheckLoopTransfers200ResponseInner`
        """
        model = CheckLoopTransfers200ResponseInner()
        if include_optional:
            return CheckLoopTransfers200ResponseInner(
                address = '0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045',
                is_loop = False
            )
        else:
            return CheckLoopTransfers200ResponseInner(
        )
        """

    def testCheckLoopTransfers200ResponseInner(self):
        """Test CheckLoopTransfers200ResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
