# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    The version of the OpenAPI document: 1.0.0
    Contact: support@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.webhook_event_data_type import WebhookEventDataType


class TestWebhookEventDataType(unittest.TestCase):
    """WebhookEventDataType unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebhookEventDataType:
        """Test WebhookEventDataType
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebhookEventDataType`
        """
        model = WebhookEventDataType()
        if include_optional:
            return WebhookEventDataType(
                data_type = 'Transaction'
            )
        else:
            return WebhookEventDataType(
                data_type = 'Transaction',
        )
        """

    def testWebhookEventDataType(self):
        """Test WebhookEventDataType"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()