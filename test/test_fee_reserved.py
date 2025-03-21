# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.fee_reserved import FeeReserved


class TestFeeReserved(unittest.TestCase):
    """FeeReserved unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FeeReserved:
        """Test FeeReserved
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FeeReserved`
        """
        model = FeeReserved()
        if include_optional:
            return FeeReserved(
                reserved_fee = '1000000000000'
            )
        else:
            return FeeReserved(
        )
        """

    def testFeeReserved(self):
        """Test FeeReserved"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
