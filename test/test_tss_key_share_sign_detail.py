# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.tss_key_share_sign_detail import TSSKeyShareSignDetail


class TestTSSKeyShareSignDetail(unittest.TestCase):
    """TSSKeyShareSignDetail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TSSKeyShareSignDetail:
        """Test TSSKeyShareSignDetail
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TSSKeyShareSignDetail`
        """
        model = TSSKeyShareSignDetail()
        if include_optional:
            return TSSKeyShareSignDetail(
                group_id = 'mMedDioOKhTlhGyQRzMv',
                message = ''
            )
        else:
            return TSSKeyShareSignDetail(
        )
        """

    def testTSSKeyShareSignDetail(self):
        """Test TSSKeyShareSignDetail"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
