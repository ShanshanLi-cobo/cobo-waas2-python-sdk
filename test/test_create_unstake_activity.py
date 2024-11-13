# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.create_unstake_activity import CreateUnstakeActivity


class TestCreateUnstakeActivity(unittest.TestCase):
    """CreateUnstakeActivity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateUnstakeActivity:
        """Test CreateUnstakeActivity
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateUnstakeActivity`
        """
        model = CreateUnstakeActivity()
        if include_optional:
            return CreateUnstakeActivity(
                request_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479',
                staking_id = '0011039d-27fb-49ba-b172-6e0aa80e37ec',
                amount = '100.00',
                fee = None,
                extra = None
            )
        else:
            return CreateUnstakeActivity(
                staking_id = '0011039d-27fb-49ba-b172-6e0aa80e37ec',
        )
        """

    def testCreateUnstakeActivity(self):
        """Test CreateUnstakeActivity"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
