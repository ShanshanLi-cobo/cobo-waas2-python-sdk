# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.list_key_share_holder_groups200_response import ListKeyShareHolderGroups200Response


class TestListKeyShareHolderGroups200Response(unittest.TestCase):
    """ListKeyShareHolderGroups200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListKeyShareHolderGroups200Response:
        """Test ListKeyShareHolderGroups200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListKeyShareHolderGroups200Response`
        """
        model = ListKeyShareHolderGroups200Response()
        if include_optional:
            return ListKeyShareHolderGroups200Response(
                data = [
                    cobo_waas2.models.key_share_holder_group.KeyShareHolderGroup(
                        key_share_holder_group_id = 'b33130a9-6e18-44a9-9e48-8b3b41921f0e', 
                        type = 'MainGroup', 
                        tss_key_share_groups = [
                            cobo_waas2.models.tss_groups.TSSGroups(
                                tss_key_share_group_id = 'mMedDioOKhTlhGyQRzMv', 
                                curve = 'SECP256K1', 
                                root_pubkey = 'xpub661MyMwAqRbcG4vPNi58VQJrXW8D9VzmauuRq2rTY3oUVnKGuLTxQxvvoEXgLvZ7N9GQXQkWVgKn1rzEUUEm4NdvrBKUqjpNJEnn2UL4rYq', )
                            ], 
                        key_share_holders = [
                            cobo_waas2.models.key_share_holder.KeyShareHolder(
                                name = 'Key share holder name', 
                                tss_node_id = 'coboAbCdEfGhIjKlMnOpQrStUvWxYz1234567890abcdefghi', 
                                online = True, 
                                signer = True, 
                                status = 'Valid', 
                                account_id = 'auth0|cobo|839305394802991371', )
                            ], 
                        participants = 3, 
                        threshold = 2, 
                        status = 'Valid', 
                        created_timestamp = 1718619403933, )
                    ],
                pagination = cobo_waas2.models.pagination.Pagination(
                    before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1', 
                    after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk', 
                    total_count = 10000, )
            )
        else:
            return ListKeyShareHolderGroups200Response(
        )
        """

    def testListKeyShareHolderGroups200Response(self):
        """Test ListKeyShareHolderGroups200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
