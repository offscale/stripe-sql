from sqlalchemy import JSON, Column, Identity, Integer, Table

from . import metadata

BankConnectionsResourceBalanceApiResourceCreditBalance.Json = Table(
    "bank_connections_resource_balance_api_resource_credit_balance.json",
    metadata,
    Column(
        "used",
        JSON,
        comment="The credit that has been used by the account holder.\n\nEach key is a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase.\n\nEach value is a integer amount. A positive amount indicates money owed to the account holder. A negative amount indicates money owed by the account holder",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["bank_connections_resource_balance_api_resource_credit_balance.json"]
