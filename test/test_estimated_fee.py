# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.estimated_fee import EstimatedFee


class TestEstimatedFee(unittest.TestCase):
    """EstimatedFee unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EstimatedFee:
        """Test EstimatedFee
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EstimatedFee`
        """
        model = EstimatedFee()
        if include_optional:
            return EstimatedFee(
                fee_type = 'EVM_EIP_1559',
                token_id = 'BTC',
                is_loop = False,
                fee_amount = '0.1',
                slow = None,
                recommended = None,
                fast = None
            )
        else:
            return EstimatedFee(
                fee_type = 'EVM_EIP_1559',
                token_id = 'BTC',
                fee_amount = '0.1',
                recommended = None,
        )
        """

    def testEstimatedFee(self):
        """Test EstimatedFee"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
