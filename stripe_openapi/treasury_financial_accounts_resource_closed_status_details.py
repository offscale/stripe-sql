from sqlalchemy import ARRAY, Column, Identity, Integer, String, Table

from . import metadata

TreasuryFinancialAccountsResourceClosedStatusDetails.Json = Table(
    "treasury_financial_accounts_resource_closed_status_details.json",
    metadata,
    Column(
        "reasons",
        ARRAY(String),
        comment="The array that contains reasons for a FinancialAccount closure",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["treasury_financial_accounts_resource_closed_status_details.json"]
