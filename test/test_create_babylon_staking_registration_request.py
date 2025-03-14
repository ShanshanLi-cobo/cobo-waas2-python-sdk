# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.create_babylon_staking_registration_request import CreateBabylonStakingRegistrationRequest


class TestCreateBabylonStakingRegistrationRequest(unittest.TestCase):
    """CreateBabylonStakingRegistrationRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateBabylonStakingRegistrationRequest:
        """Test CreateBabylonStakingRegistrationRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateBabylonStakingRegistrationRequest`
        """
        model = CreateBabylonStakingRegistrationRequest()
        if include_optional:
            return CreateBabylonStakingRegistrationRequest(
                staking_id = '3f2840ce-44eb-450b-aa81-d3f84b772efb',
                babylon_address = None
            )
        else:
            return CreateBabylonStakingRegistrationRequest(
        )
        """

    def testCreateBabylonStakingRegistrationRequest(self):
        """Test CreateBabylonStakingRegistrationRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
