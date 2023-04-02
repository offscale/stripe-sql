from sqlalchemy import Column, ForeignKey, Identity, Integer, Table

from . import metadata

TreasuryFinancialAccountsResourceFinancialAddressesFeaturesJson = Table(
    "treasury_financial_accounts_resource_financial_addresses_featuresjson",
    metadata,
    Column(
        "aba",
        TreasuryFinancialAccountsResourceToggleSettings,
        ForeignKey("TreasuryFinancialAccountsResourceToggleSettings"),
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["treasury_financial_accounts_resource_financial_addresses_features.json"]
