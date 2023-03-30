from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

TreasuryFinancialAccountsResourceTogglesSettingStatusDetails.Json = Table(
    "treasury_financial_accounts_resource_toggles_setting_status_details.json",
    metadata,
    Column(
        "code",
        String,
        comment="Represents the reason why the status is `pending` or `restricted`",
    ),
    Column(
        "resolution",
        String,
        comment="Represents what the user should do, if anything, to activate the Feature",
        nullable=True,
    ),
    Column(
        "restriction",
        String,
        comment="The `platform_restrictions` that are restricting this Feature",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["treasury_financial_accounts_resource_toggles_setting_status_details.json"]
