# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.safe_tx_extra_data import SafeTxExtraData


class TestSafeTxExtraData(unittest.TestCase):
    """SafeTxExtraData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SafeTxExtraData:
        """Test SafeTxExtraData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SafeTxExtraData`
        """
        model = SafeTxExtraData()
        if include_optional:
            return SafeTxExtraData(
                to = '0x1234567890abcdef1234567890abcdef12345678',
                value = '1 ETH',
                data = '0xabcdef...',
                domain_hash = '0xabcdef123456...',
                message_hash = '0xabcdef123456...',
                safe_address = '0xabcdefabcdefabcdefabcdefabcdefabcdef',
                safe_tx_hash = '0x123456abcdef...',
                safe_nonce = 42,
                operation = 'Call',
                gas_token_addr = '0xabcdefabcdef...',
                safe_tx_gas = 21000,
                base_gas = 5000,
                gas_price = '100',
                refund_receiver = '0xabcdefabcdef...',
                to_contract_name = 'UniswapV2Router',
                decoded_data = cobo_waas2.models.safe_tx_decoded_data.SafeTxDecodedData(
                    method = 'transfer', 
                    parameters = [
                        cobo_waas2.models.safe_tx_decoded_data_parameters.SafeTxDecodedDataParameters(
                            name = 'recipient', 
                            type = 'address', 
                            value = '0x1234567890abcdef1234567890abcdef12345678', 
                            value_decoded = [
                                cobo_waas2.models.safe_tx_sub_transaction.SafeTxSubTransaction(
                                    operation = 'Call', 
                                    to = '0xabcdefabcdefabcdefabcdefabcdefabcdef', 
                                    value = '1 ETH', 
                                    wei = '1000000000000000000', 
                                    data = '0xabcdef...', 
                                    data_decoded = cobo_waas2.models.safe_tx_decoded_data.SafeTxDecodedData(
                                        method = 'transfer', ), 
                                    to_contract_name = 'UniswapV2Router', )
                                ], )
                        ], ),
                signature = '0xabcdef123456...',
                wei = '1000000000000000000'
            )
        else:
            return SafeTxExtraData(
                to = '0x1234567890abcdef1234567890abcdef12345678',
                value = '1 ETH',
                data = '0xabcdef...',
                domain_hash = '0xabcdef123456...',
                message_hash = '0xabcdef123456...',
                safe_address = '0xabcdefabcdefabcdefabcdefabcdefabcdef',
                safe_tx_hash = '0x123456abcdef...',
                safe_nonce = 42,
                operation = 'Call',
        )
        """

    def testSafeTxExtraData(self):
        """Test SafeTxExtraData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
