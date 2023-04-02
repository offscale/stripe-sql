from sqlalchemy import ARRAY, Column, ForeignKey, Identity, Integer, String, Table

from . import metadata

TreasuryFinancialAccountsResourceFinancialAddressJson = Table(
    "treasury_financial_accounts_resource_financial_addressjson",
    metadata,
    Column(
        "aba",
        TreasuryFinancialAccountsResourceAbaRecord,
        ForeignKey("TreasuryFinancialAccountsResourceAbaRecord"),
        nullable=True,
    ),
    Column(
        "supported_networks",
        ARRAY(String),
        comment="The list of networks that the address supports",
        nullable=True,
    ),
    Column("type", String, comment="The type of financial address"),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["treasury_financial_accounts_resource_financial_address.json"]
