# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.tss_event import TSSEvent


class TestTSSEvent(unittest.TestCase):
    """TSSEvent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TSSEvent:
        """Test TSSEvent
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TSSEvent`
        """
        model = TSSEvent()
        if include_optional:
            return TSSEvent(
                event_id = '8f2e919a-6a7b-4a9b-8c1a-4c0b3f5b8b1f',
                created_timestamp = 1701396866000,
                node_id = 'coboAbCdEfGhIjKlMnOpQrStUvWxYz1234567890abcdefghi',
                event_type = 'request.keygen.succeeded',
                data = None
            )
        else:
            return TSSEvent(
                event_type = 'request.keygen.succeeded',
        )
        """

    def testTSSEvent(self):
        """Test TSSEvent"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
