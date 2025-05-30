# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.activity_extra import ActivityExtra


class TestActivityExtra(unittest.TestCase):
    """ActivityExtra unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ActivityExtra:
        """Test ActivityExtra
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ActivityExtra`
        """
        model = ActivityExtra()
        if include_optional:
            return ActivityExtra(
                pool_type = 'Babylon',
                finality_provider_public_key = 'eca1b104dce16c30705f4147a9c4a373ac88646c5d1bcda6a89c018940cb96a0',
                stake_block_time = 2000,
                auto_broadcast = False,
                provider_name = 'Stakefish',
                validator_pubkeys = ["0x1234567890987654321012345678909876543210","0x1234567890987654321012345678909876543210"],
                timelock = 1704067200,
                change_address = 'bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh',
                validator_address = '0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045',
                reward_address = '0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045'
            )
        else:
            return ActivityExtra(
                pool_type = 'Babylon',
        )
        """

    def testActivityExtra(self):
        """Test ActivityExtra"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
