from sqlalchemy import JSON, Column, ForeignKey, Integer, String, Table

from stripe_openapi.refund import Refund
from stripe_openapi.transfer import Transfer

from . import metadata

TransferReversalJson = Table(
    "transfer_reversaljson",
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
        "destination_payment_refund",
        Refund,
        ForeignKey("Refund"),
        comment="Linked payment refund for the transfer reversal",
        nullable=True,
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
    Column(
        "source_refund",
        Refund,
        ForeignKey("Refund"),
        comment="ID of the refund responsible for the transfer reversal",
        nullable=True,
    ),
    Column(
        "transfer",
        Transfer,
        ForeignKey("Transfer"),
        comment="ID of the transfer that was reversed",
    ),
)
__all__ = ["transfer_reversal.json"]
