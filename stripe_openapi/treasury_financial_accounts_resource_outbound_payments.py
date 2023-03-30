from sqlalchemy import Column, ForeignKey, Identity, Integer, Table

from . import metadata

TreasuryFinancialAccountsResourceOutboundPayments.Json = Table(
    "treasury_financial_accounts_resource_outbound_payments.json",
    metadata,
    Column(
        "ach",
        TreasuryFinancialAccountsResourceAchToggleSettings,
        ForeignKey("TreasuryFinancialAccountsResourceAchToggleSettings"),
        nullable=True,
    ),
    Column(
        "us_domestic_wire",
        TreasuryFinancialAccountsResourceToggleSettings,
        ForeignKey("TreasuryFinancialAccountsResourceToggleSettings"),
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["treasury_financial_accounts_resource_outbound_payments.json"]
