from sqlalchemy import Boolean, Column, Identity, Integer, String, Table, list

from . import metadata

TreasuryFinancialAccountsResourceAchToggleSettings.Json = Table(
    "treasury_financial_accounts_resource_ach_toggle_settings.json",
    metadata,
    Column(
        "requested",
        Boolean,
        comment="Whether the FinancialAccount should have the Feature",
    ),
    Column("status", String, comment="Whether the Feature is operational"),
    Column(
        "status_details",
        list,
        comment="Additional details; includes at least one entry when the status is not `active`",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["treasury_financial_accounts_resource_ach_toggle_settings.json"]
