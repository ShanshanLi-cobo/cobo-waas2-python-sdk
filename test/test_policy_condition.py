# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.policy_condition import PolicyCondition


class TestPolicyCondition(unittest.TestCase):
    """PolicyCondition unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PolicyCondition:
        """Test PolicyCondition
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PolicyCondition`
        """
        model = PolicyCondition()
        if include_optional:
            return PolicyCondition(
                var_field = 'amount',
                value_type = 'INT',
                value = '11.23',
                operator = '='
            )
        else:
            return PolicyCondition(
                var_field = 'amount',
                value_type = 'INT',
                value = '11.23',
                operator = '=',
        )
        """

    def testPolicyCondition(self):
        """Test PolicyCondition"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
