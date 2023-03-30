from sqlalchemy import (
    JSON,
    Boolean,
    Column,
    ForeignKey,
    Identity,
    Integer,
    String,
    Table,
)

from . import metadata

CashBalance.Json = Table(
    "cash_balance.json",
    metadata,
    Column(
        "available",
        JSON,
        comment="A hash of all cash balances available to this customer. You cannot delete a customer with any cash balances, even if the balance is 0. Amounts are represented in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal)",
        nullable=True,
    ),
    Column(
        "customer",
        String,
        comment="The ID of the customer whose cash balance this object represents",
    ),
    Column(
        "livemode",
        Boolean,
        comment="Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode",
    ),
    Column(
        "object",
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    ),
    Column(
        "settings",
        CustomerBalanceCustomerBalanceSettings,
        ForeignKey("CustomerBalanceCustomerBalanceSettings"),
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["cash_balance.json"]
