# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.stakings_extra import StakingsExtra


class TestStakingsExtra(unittest.TestCase):
    """StakingsExtra unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StakingsExtra:
        """Test StakingsExtra
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StakingsExtra`
        """
        model = StakingsExtra()
        if include_optional:
            return StakingsExtra(
                pool_type = 'Babylon',
                pos_chain = 'Babylon Chain',
                unlock_timestamp = 1640995200000,
                unlock_block_height = 871234,
                stake_address = 'tb1pgmpawe2rkrzuuflu8yw564lerfalhw8td36dha49yz4l99xvm3psteh393',
                unbond_address = 'tb1pzcn4hmsfq32vyfnckvrtyjhdh0cf2hsm2nr6m8034x4lnrx3ry4q2nyzqv'
            )
        else:
            return StakingsExtra(
                pool_type = 'Babylon',
                pos_chain = 'Babylon Chain',
        )
        """

    def testStakingsExtra(self):
        """Test StakingsExtra"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
