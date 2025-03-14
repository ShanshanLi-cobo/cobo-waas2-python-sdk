# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.estimated_evm_eip1559_fee_slow import EstimatedEvmEip1559FeeSlow


class TestEstimatedEvmEip1559FeeSlow(unittest.TestCase):
    """EstimatedEvmEip1559FeeSlow unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EstimatedEvmEip1559FeeSlow:
        """Test EstimatedEvmEip1559FeeSlow
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EstimatedEvmEip1559FeeSlow`
        """
        model = EstimatedEvmEip1559FeeSlow()
        if include_optional:
            return EstimatedEvmEip1559FeeSlow(
                max_fee_per_gas = '9000000000000',
                max_priority_fee_per_gas = '1000000000000',
                gas_limit = '21000',
                reserved_fee = '1000000000000'
            )
        else:
            return EstimatedEvmEip1559FeeSlow(
                max_fee_per_gas = '9000000000000',
                max_priority_fee_per_gas = '1000000000000',
                gas_limit = '21000',
        )
        """

    def testEstimatedEvmEip1559FeeSlow(self):
        """Test EstimatedEvmEip1559FeeSlow"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
