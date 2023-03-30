from sqlalchemy import Column, ForeignKey, Identity, Integer, Table

from . import metadata

TreasuryFinancialAccountsResourceInboundTransfers.Json = Table(
    "treasury_financial_accounts_resource_inbound_transfers.json",
    metadata,
    Column(
        "ach",
        TreasuryFinancialAccountsResourceAchToggleSettings,
        ForeignKey("TreasuryFinancialAccountsResourceAchToggleSettings"),
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["treasury_financial_accounts_resource_inbound_transfers.json"]
