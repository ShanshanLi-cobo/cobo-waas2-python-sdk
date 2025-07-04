# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.get_settlement_info_by_ids200_response import GetSettlementInfoByIds200Response


class TestGetSettlementInfoByIds200Response(unittest.TestCase):
    """GetSettlementInfoByIds200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetSettlementInfoByIds200Response:
        """Test GetSettlementInfoByIds200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetSettlementInfoByIds200Response`
        """
        model = GetSettlementInfoByIds200Response()
        if include_optional:
            return GetSettlementInfoByIds200Response(
                psp_token_balances = [
                    cobo_waas2.models.settlement_info.SettlementInfo(
                        merchant_id = '123', 
                        token_id = 'ETH_USDT', 
                        available_amount = '500.00', 
                        available_currency_balance = '500.00', 
                        pending_amount = '500.00', 
                        pending_currency_balance = '500.00', 
                        settled_amount = '500.00', 
                        acquiring_type = 'Order', 
                        created_timestamp = 1744689600, 
                        updated_timestamp = 1744689600, )
                    ],
                token_balances = [
                    cobo_waas2.models.settlement_info.SettlementInfo(
                        merchant_id = '123', 
                        token_id = 'ETH_USDT', 
                        available_amount = '500.00', 
                        available_currency_balance = '500.00', 
                        pending_amount = '500.00', 
                        pending_currency_balance = '500.00', 
                        settled_amount = '500.00', 
                        acquiring_type = 'Order', 
                        created_timestamp = 1744689600, 
                        updated_timestamp = 1744689600, )
                    ]
            )
        else:
            return GetSettlementInfoByIds200Response(
        )
        """

    def testGetSettlementInfoByIds200Response(self):
        """Test GetSettlementInfoByIds200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
