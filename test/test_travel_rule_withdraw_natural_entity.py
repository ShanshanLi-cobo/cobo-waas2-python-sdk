# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.travel_rule_withdraw_natural_entity import TravelRuleWithdrawNaturalEntity


class TestTravelRuleWithdrawNaturalEntity(unittest.TestCase):
    """TravelRuleWithdrawNaturalEntity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TravelRuleWithdrawNaturalEntity:
        """Test TravelRuleWithdrawNaturalEntity
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TravelRuleWithdrawNaturalEntity`
        """
        model = TravelRuleWithdrawNaturalEntity()
        if include_optional:
            return TravelRuleWithdrawNaturalEntity(
                selected_entity_type = 'LEGAL',
                first_name = 'John',
                last_name = 'Doe',
                date_of_birth = 'Tue Jan 01 00:00:00 UTC 1980',
                place_of_birth = 'City, Country'
            )
        else:
            return TravelRuleWithdrawNaturalEntity(
                selected_entity_type = 'LEGAL',
                first_name = 'John',
                last_name = 'Doe',
        )
        """

    def testTravelRuleWithdrawNaturalEntity(self):
        """Test TravelRuleWithdrawNaturalEntity"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
