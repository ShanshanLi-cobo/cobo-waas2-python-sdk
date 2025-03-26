# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.webhook_event_data import WebhookEventData


class TestWebhookEventData(unittest.TestCase):
    """WebhookEventData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebhookEventData:
        """Test WebhookEventData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebhookEventData`
        """
        model = WebhookEventData()
        if include_optional:
            return WebhookEventData(
                data_type = 'Transaction',
                transaction_id = 'aff0e1cb-15b2-4e1f-9b9d-a9133715986f',
                cobo_id = '20231213122855000000000000000000',
                request_id = '760a1955-e212-4dfb-a8d0-e66312a1a051',
                wallet_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479',
                type = 'Org-Controlled',
                status = 'Success',
                sub_status = 'PendingDoubleCheck',
                failed_reason = 'Rejected by signer Cobo TSS',
                chain_id = 'ETH',
                token_id = 'ETH_USDT',
                asset_id = 'USDT',
                source = None,
                destination = None,
                result = None,
                fee = None,
                initiator = 'API Prod Key #1',
                initiator_type = 'API',
                confirmed_num = 12,
                confirming_threshold = 15,
                transaction_hash = '239861be9a4afe080c359b7fe4a1d035945ec46256b1a0f44d1267c71de8ec28',
                block_info = cobo_waas2.models.transaction_block_info.TransactionBlockInfo(
                    block_number = 123, 
                    block_timestamp = 1717740319, 
                    block_hash = '0xc9ee947f8bb6027c161888bf0d004bec05e7c2beec7e6b187dc512174e438735', ),
                raw_tx_info = cobo_waas2.models.transaction_raw_tx_info.TransactionRawTxInfo(
                    used_nonce = 9, 
                    selected_utxos = [
                        cobo_waas2.models.transaction_selected_utxo.TransactionSelectedUtxo(
                            tx_hash = '7014d7d9b91862d7131f7543d84da3bec60e20be93c23ad01167c48b778fdemo', 
                            vout_n = 0, 
                            address = '2N2xFZtbCFB6Nb3Pj9Sxsx5mX2fxX3yEgkE', 
                            value = '0.5', 
                            redeem_script = '0x1cc56cbbac4622082221a8768d1d0901', 
                            revealed_script = '0x1cc56cbbac4622082221a8768d1d0901', )
                        ], 
                    raw_tx = '0xa22cb4650000000000000000000000001e0049783f008a0085193e00003d00cd54003c71000000000000000000000000000000000000000000000000000000000000DEMO', 
                    unsigned_raw_tx = '0xa22cb4650000000000000000000000001e0049783f008a0085193e00003d00cd54003c71000000000000000000000000000000000000000000000000000000000000DEMO', 
                    utxo_change = cobo_waas2.models.transaction_utxo_change.TransactionUtxoChange(
                        address = '2N2xFZtbCFB6Nb3Pj9Sxsx5mX2fxX3yEgkE', 
                        value = '0.5', ), ),
                replacement = cobo_waas2.models.transaction_replacement.Transaction_replacement(
                    replaced_by_type = 'Resend', 
                    replaced_by_transaction_id = 'aff0e1cb-15b2-4e1f-9b9d-a9133715986f', 
                    replaced_by_transaction_hash = '239861be9a4afe080c359b7fe4a1d035945ec46256b1a0f44d1267c71de8ec28', 
                    replaced_type = 'Resend', 
                    replaced_transaction_id = 'aff0e1cb-15b2-4e1f-9b9d-a9133715986f', 
                    replaced_transaction_hash = '239861be9a4afe080c359b7fe4a1d035945ec46256b1a0f44d1267c71de8ec28', ),
                category = [
                    'Payment'
                    ],
                description = 'This is a request to create key shares using the Recovery Group for a key share holder in the Main Group if their key share has been lost (e.g. by losing their phone).',
                is_loop = False,
                cobo_category = [
                    'AutoFueling'
                    ],
                fueling_info = cobo_waas2.models.transaction_fueling_info.TransactionFuelingInfo(
                    request_id = 'gas_760a1955-e212-4dfb-a8d0-e66312a1a051', 
                    transaction_id = 'b0530b27-104f-4338-87de-de01500326ea', ),
                created_timestamp = 1718619403933,
                updated_timestamp = 1610445878970,
                tss_request_id = '20240711114129000132315000003970',
                source_key_share_holder_group = cobo_waas2.models.source_group.SourceGroup(
                    key_share_holder_group_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479', 
                    tss_node_ids = [
                        'cobo5yb7BNEBwwp5XXedbhnzQfvQtp132W4dH4Jz4x4eDp4KA'
                        ], ),
                target_key_share_holder_group_id = 'fd9519ae-507b-4605-b108-04d4e5ffcdd3',
                addresses = [
                    null
                    ],
                wallet = None,
                vault_id = 'YPdbyVaVGqXXjkUsohHw',
                project_id = '0111039d-27fb-49ba-b172-6e0aa80e37ec',
                name = 'Vault name',
                root_pubkeys = [
                    cobo_waas2.models.root_pubkey.RootPubkey(
                        root_pubkey = 'xpub661MyMwAqRbcG4vPNi58VQJrXW8D9VzmauuRq2rTY3oUVnKGuLTxQxvvoEXgLvZ7N9GQXQkWVgKn1rzEUUEm4NdvrBKUqjpNJEnn2UL4rYq', 
                        curve = 'SECP256K1', )
                    ],
                chains = [
                    cobo_waas2.models.chain_info.ChainInfo(
                        chain_id = 'ETH', 
                        symbol = 'ETH', 
                        icon_url = 'https://d.cobo.com/public/logos/ETH.png', 
                        explorer_tx_url = 'https://etherscan.io/tx/{txn_id}', 
                        explorer_address_url = 'https://etherscan.io/address/{address}', 
                        require_memo = False, 
                        confirming_threshold = 15, )
                    ],
                tokens = [
                    cobo_waas2.models.token_info.TokenInfo(
                        token_id = 'ETH_USDT', 
                        chain_id = 'ETH', 
                        asset_id = 'USDT', 
                        symbol = 'USDT', 
                        name = 'Tether USDT', 
                        decimal = 18, 
                        icon_url = 'https://d.cobo.com/public/logos/USDT.png', 
                        token_address = '0xdAC17F958D2ee523a2206206994597C13D831ec7', 
                        fee_token_id = 'ETH', 
                        can_deposit = True, 
                        can_withdraw = True, 
                        dust_threshold = '0.00000546', 
                        custodial_minimum_deposit_threshold = '0.0001', 
                        asset_model_type = 'Account', )
                    ]
            )
        else:
            return WebhookEventData(
                data_type = 'Transaction',
                transaction_id = 'aff0e1cb-15b2-4e1f-9b9d-a9133715986f',
                wallet_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479',
                status = 'Success',
                source = None,
                destination = None,
                initiator_type = 'API',
                chains = [
                    cobo_waas2.models.chain_info.ChainInfo(
                        chain_id = 'ETH', 
                        symbol = 'ETH', 
                        icon_url = 'https://d.cobo.com/public/logos/ETH.png', 
                        explorer_tx_url = 'https://etherscan.io/tx/{txn_id}', 
                        explorer_address_url = 'https://etherscan.io/address/{address}', 
                        require_memo = False, 
                        confirming_threshold = 15, )
                    ],
                tokens = [
                    cobo_waas2.models.token_info.TokenInfo(
                        token_id = 'ETH_USDT', 
                        chain_id = 'ETH', 
                        asset_id = 'USDT', 
                        symbol = 'USDT', 
                        name = 'Tether USDT', 
                        decimal = 18, 
                        icon_url = 'https://d.cobo.com/public/logos/USDT.png', 
                        token_address = '0xdAC17F958D2ee523a2206206994597C13D831ec7', 
                        fee_token_id = 'ETH', 
                        can_deposit = True, 
                        can_withdraw = True, 
                        dust_threshold = '0.00000546', 
                        custodial_minimum_deposit_threshold = '0.0001', 
                        asset_model_type = 'Account', )
                    ],
        )
        """

    def testWebhookEventData(self):
        """Test WebhookEventData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
