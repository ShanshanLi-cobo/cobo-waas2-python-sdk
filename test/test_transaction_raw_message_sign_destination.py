# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.transaction_raw_message_sign_destination import TransactionRawMessageSignDestination


class TestTransactionRawMessageSignDestination(unittest.TestCase):
    """TransactionRawMessageSignDestination unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TransactionRawMessageSignDestination:
        """Test TransactionRawMessageSignDestination
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TransactionRawMessageSignDestination`
        """
        model = TransactionRawMessageSignDestination()
        if include_optional:
            return TransactionRawMessageSignDestination(
                destination_type = 'Address',
                msg_hash = ''
            )
        else:
            return TransactionRawMessageSignDestination(
                destination_type = 'Address',
        )
        """

    def testTransactionRawMessageSignDestination(self):
        """Test TransactionRawMessageSignDestination"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
