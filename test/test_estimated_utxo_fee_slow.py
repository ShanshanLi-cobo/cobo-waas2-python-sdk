# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.estimated_utxo_fee_slow import EstimatedUtxoFeeSlow


class TestEstimatedUtxoFeeSlow(unittest.TestCase):
    """EstimatedUtxoFeeSlow unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EstimatedUtxoFeeSlow:
        """Test EstimatedUtxoFeeSlow
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EstimatedUtxoFeeSlow`
        """
        model = EstimatedUtxoFeeSlow()
        if include_optional:
            return EstimatedUtxoFeeSlow(
                fee_rate = '50',
                fee_amount = '0.1'
            )
        else:
            return EstimatedUtxoFeeSlow(
                fee_rate = '50',
                fee_amount = '0.1',
        )
        """

    def testEstimatedUtxoFeeSlow(self):
        """Test EstimatedUtxoFeeSlow"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
