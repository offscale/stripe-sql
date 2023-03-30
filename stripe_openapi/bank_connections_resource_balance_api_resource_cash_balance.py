from sqlalchemy import JSON, Column, Identity, Integer, Table

from . import metadata

BankConnectionsResourceBalanceApiResourceCashBalance.Json = Table(
    "bank_connections_resource_balance_api_resource_cash_balance.json",
    metadata,
    Column(
        "available",
        JSON,
        comment="The funds available to the account holder. Typically this is the current balance less any holds.\n\nEach key is a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase.\n\nEach value is a integer amount. A positive amount indicates money owed to the account holder. A negative amount indicates money owed by the account holder",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["bank_connections_resource_balance_api_resource_cash_balance.json"]
