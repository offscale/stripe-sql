from sqlalchemy import Boolean, Column, Identity, Integer, String, Table

from . import metadata

CustomerBalanceCustomerBalanceSettingsJson = Table(
    "customer_balance_customer_balance_settingsjson",
    metadata,
    Column(
        "reconciliation_mode",
        String,
        comment="The configuration for how funds that land in the customer cash balance are reconciled",
    ),
    Column(
        "using_merchant_default",
        Boolean,
        comment="A flag to indicate if reconciliation mode returned is the user's default or is specific to this customer cash balance",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["customer_balance_customer_balance_settings.json"]
