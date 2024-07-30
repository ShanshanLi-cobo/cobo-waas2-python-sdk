# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    The version of the OpenAPI document: 1.0.0
    Contact: support@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.tss_groups import TSSGroups


class TestTSSGroups(unittest.TestCase):
    """TSSGroups unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TSSGroups:
        """Test TSSGroups
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TSSGroups`
        """
        model = TSSGroups()
        if include_optional:
            return TSSGroups(
                tss_key_share_group_id = 'mMedDioOKhTlhGyQRzMv',
                curve = 'ED25519'
            )
        else:
            return TSSGroups(
        )
        """

    def testTSSGroups(self):
        """Test TSSGroups"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()