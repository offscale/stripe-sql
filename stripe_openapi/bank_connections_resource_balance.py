from sqlalchemy import JSON, Column, ForeignKey, Identity, Integer, String, Table

from . import metadata

BankConnectionsResourceBalance.Json = Table(
    "bank_connections_resource_balance.json",
    metadata,
    Column(
        "as_of",
        Integer,
        comment="The time that the external institution calculated this balance. Measured in seconds since the Unix epoch",
    ),
    Column(
        "cash",
        BankConnectionsResourceBalanceApiResourceCashBalance,
        ForeignKey("BankConnectionsResourceBalanceApiResourceCashBalance"),
        nullable=True,
    ),
    Column(
        "credit",
        BankConnectionsResourceBalanceApiResourceCreditBalance,
        ForeignKey("BankConnectionsResourceBalanceApiResourceCreditBalance"),
        nullable=True,
    ),
    Column(
        "current",
        JSON,
        comment="The balances owed to (or by) the account holder.\n\nEach key is a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase.\n\nEach value is a integer amount. A positive amount indicates money owed to the account holder. A negative amount indicates money owed by the account holder",
    ),
    Column(
        "type",
        String,
        comment="The `type` of the balance. An additional hash is included on the balance with a name matching this value",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["bank_connections_resource_balance.json"]
