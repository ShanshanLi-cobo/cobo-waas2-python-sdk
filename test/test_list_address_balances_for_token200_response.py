# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.list_address_balances_for_token200_response import ListAddressBalancesForToken200Response


class TestListAddressBalancesForToken200Response(unittest.TestCase):
    """ListAddressBalancesForToken200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListAddressBalancesForToken200Response:
        """Test ListAddressBalancesForToken200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListAddressBalancesForToken200Response`
        """
        model = ListAddressBalancesForToken200Response()
        if include_optional:
            return ListAddressBalancesForToken200Response(
                data = [
                    cobo_waas2.models.address_balance.AddressBalance(
                        address = '0x0000000000000000000000000000000000000000', 
                        balance = cobo_waas2.models.balance.Balance(
                            total = '100.0', 
                            available = '80.5', 
                            pending = '0', 
                            locked = '0', ), )
                    ],
                pagination = cobo_waas2.models.pagination.Pagination(
                    before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1', 
                    after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk', 
                    total_count = 10000, )
            )
        else:
            return ListAddressBalancesForToken200Response(
        )
        """

    def testListAddressBalancesForToken200Response(self):
        """Test ListAddressBalancesForToken200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
