# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.babylon_stake_estimated_fee import BabylonStakeEstimatedFee


class TestBabylonStakeEstimatedFee(unittest.TestCase):
    """BabylonStakeEstimatedFee unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BabylonStakeEstimatedFee:
        """Test BabylonStakeEstimatedFee
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BabylonStakeEstimatedFee`
        """
        model = BabylonStakeEstimatedFee()
        if include_optional:
            return BabylonStakeEstimatedFee(
                pool_type = 'Babylon',
                fee_type = 'EVM_EIP_1559',
                fee_amount = '0.02',
                token_id = 'BTC'
            )
        else:
            return BabylonStakeEstimatedFee(
        )
        """

    def testBabylonStakeEstimatedFee(self):
        """Test BabylonStakeEstimatedFee"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()