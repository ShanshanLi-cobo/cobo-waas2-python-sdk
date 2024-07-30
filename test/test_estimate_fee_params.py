# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    The version of the OpenAPI document: 1.0.0
    Contact: support@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.estimate_fee_params import EstimateFeeParams


class TestEstimateFeeParams(unittest.TestCase):
    """EstimateFeeParams unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EstimateFeeParams:
        """Test EstimateFeeParams
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EstimateFeeParams`
        """
        model = EstimateFeeParams()
        if include_optional:
            return EstimateFeeParams(
                request_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479',
                request_type = 'Transfer',
                source = None,
                token_id = 'ETH_USDT',
                destination = None,
                fee_type = 'EVM_EIP_1559',
                chain_id = 'ETH'
            )
        else:
            return EstimateFeeParams(
                request_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479',
                request_type = 'Transfer',
                source = None,
                token_id = 'ETH_USDT',
                destination = None,
                chain_id = 'ETH',
        )
        """

    def testEstimateFeeParams(self):
        """Test EstimateFeeParams"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()