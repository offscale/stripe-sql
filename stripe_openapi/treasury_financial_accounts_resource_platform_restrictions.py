from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

TreasuryFinancialAccountsResourcePlatformRestrictionsJson = Table(
    "treasury_financial_accounts_resource_platform_restrictionsjson",
    metadata,
    Column(
        "inbound_flows",
        String,
        comment="Restricts all inbound money movement",
        nullable=True,
    ),
    Column(
        "outbound_flows",
        String,
        comment="Restricts all outbound money movement",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["treasury_financial_accounts_resource_platform_restrictions.json"]
