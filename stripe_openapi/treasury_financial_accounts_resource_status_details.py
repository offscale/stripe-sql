from sqlalchemy import Column, ForeignKey, Identity, Integer, Table

from . import metadata

TreasuryFinancialAccountsResourceStatusDetails.Json = Table(
    "treasury_financial_accounts_resource_status_details.json",
    metadata,
    Column(
        "closed",
        TreasuryFinancialAccountsResourceClosedStatusDetails,
        ForeignKey("TreasuryFinancialAccountsResourceClosedStatusDetails"),
        comment="Details related to the closure of this FinancialAccount",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["treasury_financial_accounts_resource_status_details.json"]
