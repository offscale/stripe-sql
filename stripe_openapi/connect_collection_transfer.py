from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table

from stripe_openapi.account import Account

from . import metadata

ConnectCollectionTransfer.Json = Table(
    "connect_collection_transfer.json",
    metadata,
    Column("amount", Integer, comment="Amount transferred, in %s"),
    Column(
        "currency",
        String,
        comment="Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)",
    ),
    Column(
        "destination",
        Account,
        ForeignKey("Account"),
        comment="ID of the account that funds are being collected for",
    ),
    Column("id", String, comment="Unique identifier for the object", primary_key=True),
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
)
__all__ = ["connect_collection_transfer.json"]
