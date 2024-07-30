# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    The version of the OpenAPI document: 1.0.0
    Contact: support@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.evm_eip191_message_sign_destination import EvmEIP191MessageSignDestination


class TestEvmEIP191MessageSignDestination(unittest.TestCase):
    """EvmEIP191MessageSignDestination unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EvmEIP191MessageSignDestination:
        """Test EvmEIP191MessageSignDestination
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EvmEIP191MessageSignDestination`
        """
        model = EvmEIP191MessageSignDestination()
        if include_optional:
            return EvmEIP191MessageSignDestination(
                destination_type = 'EVM_EIP_191_Signature',
                message = 'YWFhYQ=='
            )
        else:
            return EvmEIP191MessageSignDestination(
                destination_type = 'EVM_EIP_191_Signature',
                message = 'YWFhYQ==',
        )
        """

    def testEvmEIP191MessageSignDestination(self):
        """Test EvmEIP191MessageSignDestination"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()