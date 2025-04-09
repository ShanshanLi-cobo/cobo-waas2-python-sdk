# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.swap_activity import SwapActivity


class TestSwapActivity(unittest.TestCase):
    """SwapActivity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SwapActivity:
        """Test SwapActivity
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SwapActivity`
        """
        model = SwapActivity()
        if include_optional:
            return SwapActivity(
                activity_id = '123e4567-e89b-12d3-a456-426614174000',
                activity_type = 'Bridge',
                status = 'Success',
                request_id = '123e4567-e89b-12d3-a456-426614174000',
                wallet_id = '123e4567-e89b-12d3-a456-426614174001',
                pay_token_id = 'BTC',
                receive_token_id = 'ETH_WBTC',
                pay_amount = '100',
                receive_amount = '100',
                fee_amount = '0.3',
                initiator = 'John Doe',
                initiator_type = 'API',
                description = 'This is a description of the swap activity.',
                created_timestamp = 1677587333000,
                updated_timestamp = 1677587393000
            )
        else:
            return SwapActivity(
        )
        """

    def testSwapActivity(self):
        """Test SwapActivity"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
