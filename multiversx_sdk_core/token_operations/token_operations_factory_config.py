from multiversx_sdk_core.address import Address
from multiversx_sdk_core.interfaces import (IAddress, IChainID, IGasLimit,
                                            IGasPrice, ITransactionValue)


class TokenOperationsFactoryConfig:
    def __init__(self, chain_id: IChainID) -> None:
        self.chain_id: IChainID = chain_id
        self.min_gas_price: IGasPrice = 1000000000
        self.min_gas_limit: IGasLimit = 50_000
        self.gas_limit_per_byte: IGasLimit = 1_500
        self.gas_limit_issue: IGasLimit = 60_000_000
        self.gas_limit_toggle_burn_role_globally: IGasLimit = 60_000_000
        self.gas_limit_esdt_local_mint: IGasLimit = 300_000
        self.gas_limit_esdt_local_burn: IGasLimit = 300_000
        self.gas_limit_set_special_role: IGasLimit = 60_000_000
        self.gas_limit_pausing: IGasLimit = 60_000_000
        self.gas_limit_freezing: IGasLimit = 60_000_000
        self.gas_limit_wiping: IGasLimit = 60_000_000
        self.gas_limit_esdt_nft_create: IGasLimit = 3_000_000
        self.gas_limit_esdt_nft_update_attributes: IGasLimit = 1_000_000
        self.gas_limit_esdt_nft_add_quantity: IGasLimit = 1_000_000
        self.gas_limit_esdt_nft_burn: IGasLimit = 1_000_000
        self.gas_limit_store_per_byte: IGasLimit = 50_000
        self.issue_cost: ITransactionValue = 50_000_000_000_000_000
        self.esdt_contract_address: IAddress = Address.from_bech32("erd1qqqqqqqqqqqqqqqpqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqzllls8a5w6u")