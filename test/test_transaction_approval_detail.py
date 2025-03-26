# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.transaction_approval_detail import TransactionApprovalDetail


class TestTransactionApprovalDetail(unittest.TestCase):
    """TransactionApprovalDetail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TransactionApprovalDetail:
        """Test TransactionApprovalDetail
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TransactionApprovalDetail`
        """
        model = TransactionApprovalDetail()
        if include_optional:
            return TransactionApprovalDetail(
                transaction_id = 'aff0e1cb-15b2-4e1f-9b9d-a9133715986f',
                cobo_id = '20231213122855000000000000000000',
                request_id = 'web_send_by_user_327_1610444045047',
                spender = cobo_waas2.models.transaction_role_approval_detail.TransactionRoleApprovalDetail(
                    result = 'Approved', 
                    review_threshold = 1, 
                    initiator = 'tom@gmail.com', 
                    complete_time = '', 
                    user_details = [
                        cobo_waas2.models.transaction_user_approval_detail.TransactionUserApprovalDetail(
                            name = 'tom', 
                            email = 'tom@gmail.com', 
                            pubkey = '96db1b3c68c3a3497bffb7e257a3900b0e86575c968a346a6696d1676fa8c5a6431b46c867134bd5fb8a9b5f787fa0c534d7c7664f1e52c432ce64326cc4cc1d', 
                            signature = '', 
                            language = 'en', 
                            message_version = '1.0.1', 
                            message = '', 
                            extra_message = '', )
                        ], ),
                approver = cobo_waas2.models.transaction_role_approval_detail.TransactionRoleApprovalDetail(
                    result = 'Approved', 
                    review_threshold = 1, 
                    initiator = 'tom@gmail.com', 
                    complete_time = '', 
                    user_details = [
                        cobo_waas2.models.transaction_user_approval_detail.TransactionUserApprovalDetail(
                            name = 'tom', 
                            email = 'tom@gmail.com', 
                            pubkey = '96db1b3c68c3a3497bffb7e257a3900b0e86575c968a346a6696d1676fa8c5a6431b46c867134bd5fb8a9b5f787fa0c534d7c7664f1e52c432ce64326cc4cc1d', 
                            signature = '', 
                            language = 'en', 
                            message_version = '1.0.1', 
                            message = '', 
                            extra_message = '', )
                        ], ),
                address_owner = cobo_waas2.models.transaction_role_approval_detail.TransactionRoleApprovalDetail(
                    result = 'Approved', 
                    review_threshold = 1, 
                    initiator = 'tom@gmail.com', 
                    complete_time = '', 
                    user_details = [
                        cobo_waas2.models.transaction_user_approval_detail.TransactionUserApprovalDetail(
                            name = 'tom', 
                            email = 'tom@gmail.com', 
                            pubkey = '96db1b3c68c3a3497bffb7e257a3900b0e86575c968a346a6696d1676fa8c5a6431b46c867134bd5fb8a9b5f787fa0c534d7c7664f1e52c432ce64326cc4cc1d', 
                            signature = '', 
                            language = 'en', 
                            message_version = '1.0.1', 
                            message = '', 
                            extra_message = '', )
                        ], )
            )
        else:
            return TransactionApprovalDetail(
        )
        """

    def testTransactionApprovalDetail(self):
        """Test TransactionApprovalDetail"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
