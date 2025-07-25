# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.get_max_transferable_value_with_fee_model_request import GetMaxTransferableValueWithFeeModelRequest


class TestGetMaxTransferableValueWithFeeModelRequest(unittest.TestCase):
    """GetMaxTransferableValueWithFeeModelRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetMaxTransferableValueWithFeeModelRequest:
        """Test GetMaxTransferableValueWithFeeModelRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetMaxTransferableValueWithFeeModelRequest`
        """
        model = GetMaxTransferableValueWithFeeModelRequest()
        if include_optional:
            return GetMaxTransferableValueWithFeeModelRequest(
                token_id = 'ETH_USDT',
                fee = None,
                to_address = '2N2xFZtbCFB6Nb3Pj9Sxsx5mX2fxX3yEgkE',
                from_address = '2N2xFZtbCFB6Nb3Pj9Sxsx5mX2fxX3yEgkE'
            )
        else:
            return GetMaxTransferableValueWithFeeModelRequest(
                token_id = 'ETH_USDT',
                fee = None,
                to_address = '2N2xFZtbCFB6Nb3Pj9Sxsx5mX2fxX3yEgkE',
        )
        """

    def testGetMaxTransferableValueWithFeeModelRequest(self):
        """Test GetMaxTransferableValueWithFeeModelRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
