# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.create_webhook_endpoint_request import CreateWebhookEndpointRequest


class TestCreateWebhookEndpointRequest(unittest.TestCase):
    """CreateWebhookEndpointRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateWebhookEndpointRequest:
        """Test CreateWebhookEndpointRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateWebhookEndpointRequest`
        """
        model = CreateWebhookEndpointRequest()
        if include_optional:
            return CreateWebhookEndpointRequest(
                url = 'https://example.com/webhook',
                subscribed_events = [
                    'wallets.transaction.created'
                    ],
                description = 'My webhook endpoint'
            )
        else:
            return CreateWebhookEndpointRequest(
                url = 'https://example.com/webhook',
                subscribed_events = [
                    'wallets.transaction.created'
                    ],
        )
        """

    def testCreateWebhookEndpointRequest(self):
        """Test CreateWebhookEndpointRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
