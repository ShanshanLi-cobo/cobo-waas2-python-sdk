# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.list_babylon_eligible_stakings200_response_data_inner import ListBabylonEligibleStakings200ResponseDataInner


class TestListBabylonEligibleStakings200ResponseDataInner(unittest.TestCase):
    """ListBabylonEligibleStakings200ResponseDataInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListBabylonEligibleStakings200ResponseDataInner:
        """Test ListBabylonEligibleStakings200ResponseDataInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListBabylonEligibleStakings200ResponseDataInner`
        """
        model = ListBabylonEligibleStakings200ResponseDataInner()
        if include_optional:
            return ListBabylonEligibleStakings200ResponseDataInner(
                staking_id = '0011039d-27fb-49ba-b172-6e0aa80e37ec',
                btc_address = None,
                babylon_address = None,
                staked_amount = '1.23456789',
                status = 'Registered'
            )
        else:
            return ListBabylonEligibleStakings200ResponseDataInner(
        )
        """

    def testListBabylonEligibleStakings200ResponseDataInner(self):
        """Test ListBabylonEligibleStakings200ResponseDataInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
