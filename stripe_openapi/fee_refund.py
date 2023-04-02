from sqlalchemy import JSON, Column, ForeignKey, Integer, String, Table

from . import metadata

FeeRefundJson = Table(
    "fee_refundjson",
    metadata,
    Column("amount", Integer, comment="Amount, in %s"),
    Column(
        "balance_transaction",
        BalanceTransaction,
        ForeignKey("BalanceTransaction"),
        comment="Balance transaction that describes the impact on your account balance",
        nullable=True,
    ),
    Column(
        "created",
        Integer,
        comment="Time at which the object was created. Measured in seconds since the Unix epoch",
    ),
    Column(
        "currency",
        String,
        comment="Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)",
    ),
    Column(
        "fee",
        ApplicationFee,
        ForeignKey("ApplicationFee"),
        comment="ID of the application fee that was refunded",
    ),
    Column("id", String, comment="Unique identifier for the object", primary_key=True),
    Column(
        "metadata",
        JSON,
        comment="Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format",
        nullable=True,
    ),
    Column(
        "object",
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    ),
)
__all__ = ["fee_refund.json"]
