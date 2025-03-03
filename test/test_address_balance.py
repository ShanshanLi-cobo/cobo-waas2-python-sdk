# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.address_balance import AddressBalance


class TestAddressBalance(unittest.TestCase):
    """AddressBalance unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AddressBalance:
        """Test AddressBalance
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AddressBalance`
        """
        model = AddressBalance()
        if include_optional:
            return AddressBalance(
                address = '0x0000000000000000000000000000000000000000',
                balance = cobo_waas2.models.balance.Balance(
                    total = '100.0', 
                    available = '80.5', 
                    pending = '0', 
                    locked = '0', )
            )
        else:
            return AddressBalance(
                address = '0x0000000000000000000000000000000000000000',
                balance = cobo_waas2.models.balance.Balance(
                    total = '100.0', 
                    available = '80.5', 
                    pending = '0', 
                    locked = '0', ),
        )
        """

    def testAddressBalance(self):
        """Test AddressBalance"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
