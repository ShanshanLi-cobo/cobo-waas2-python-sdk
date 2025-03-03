# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.list_swap_activities200_response import ListSwapActivities200Response


class TestListSwapActivities200Response(unittest.TestCase):
    """ListSwapActivities200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListSwapActivities200Response:
        """Test ListSwapActivities200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListSwapActivities200Response`
        """
        model = ListSwapActivities200Response()
        if include_optional:
            return ListSwapActivities200Response(
                data = [
                    cobo_waas2.models.swap_activity.SwapActivity(
                        activity_id = '123e4567-e89b-12d3-a456-426614174000', 
                        status = 'Success', 
                        wallet_id = '123e4567-e89b-12d3-a456-426614174001', 
                        pay_token_id = 'BTC', 
                        receive_token_id = 'ETH_WBTC', 
                        pay_amount = '100', 
                        receive_amount = '100', 
                        fee_amount = '0.3', 
                        initiator = 'John Doe', 
                        initiator_type = 'API', 
                        created_timestamp = 1677587333000, 
                        updated_timestamp = 1677587393000, )
                    ],
                pagination = cobo_waas2.models.pagination.Pagination(
                    before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1', 
                    after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk', 
                    total_count = 10000, )
            )
        else:
            return ListSwapActivities200Response(
        )
        """

    def testListSwapActivities200Response(self):
        """Test ListSwapActivities200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
