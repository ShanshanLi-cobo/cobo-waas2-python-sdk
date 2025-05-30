# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.transaction_role_approval_detail import TransactionRoleApprovalDetail


class TestTransactionRoleApprovalDetail(unittest.TestCase):
    """TransactionRoleApprovalDetail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TransactionRoleApprovalDetail:
        """Test TransactionRoleApprovalDetail
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TransactionRoleApprovalDetail`
        """
        model = TransactionRoleApprovalDetail()
        if include_optional:
            return TransactionRoleApprovalDetail(
                result = 'Approved',
                review_threshold = 1,
                initiator = 'tom@gmail.com',
                complete_time = '',
                user_details = [
                    cobo_waas2.models.transaction_user_approval_detail.TransactionUserApprovalDetail(
                        name = 'tom', 
                        email = 'tom@gmail.com', 
                        pubkey = '96db1b3c68c3a3497bffb7e257a3900b0e86575c968a346a6696d1676fa8c5a6431b46c867134bd5fb8a9b5f787fa0c534d7c7664f1e52c432ce64326cc4cc1d', 
                        result = 'Approved', 
                        signature = '', 
                        language = 'en', 
                        message_version = '1.0.1', 
                        message = '', 
                        extra_message = '', )
                    ]
            )
        else:
            return TransactionRoleApprovalDetail(
        )
        """

    def testTransactionRoleApprovalDetail(self):
        """Test TransactionRoleApprovalDetail"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
