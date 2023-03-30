from sqlalchemy import JSON, Boolean, Column, ForeignKey, Integer, String, Table

from stripe_openapi.source import Source

from . import metadata

Topup.Json = Table(
    "topup.json",
    metadata,
    Column("amount", Integer, comment="Amount transferred"),
    Column(
        "balance_transaction",
        BalanceTransaction,
        ForeignKey("BalanceTransaction"),
        comment="ID of the balance transaction that describes the impact of this top-up on your account balance. May not be specified depending on status of top-up",
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
        "description",
        String,
        comment="An arbitrary string attached to the object. Often useful for displaying to users",
        nullable=True,
    ),
    Column(
        "expected_availability_date",
        Integer,
        comment="Date the funds are expected to arrive in your Stripe account for payouts. This factors in delays like weekends or bank holidays. May not be specified depending on status of top-up",
        nullable=True,
    ),
    Column(
        "failure_code",
        String,
        comment="Error code explaining reason for top-up failure if available (see [the errors section](https://stripe.com/docs/api#errors) for a list of codes)",
        nullable=True,
    ),
    Column(
        "failure_message",
        String,
        comment="Message to user further explaining reason for top-up failure if available",
        nullable=True,
    ),
    Column("id", String, comment="Unique identifier for the object", primary_key=True),
    Column(
        "livemode",
        Boolean,
        comment="Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode",
    ),
    Column(
        "metadata",
        JSON,
        comment="Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format",
    ),
    Column(
        "object",
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    ),
    Column(
        "source",
        Source,
        ForeignKey("Source"),
        comment="For most Stripe users, the source of every top-up is a bank account. This hash is then the [source object](https://stripe.com/docs/api#source_object) describing that bank account",
        nullable=True,
    ),
    Column(
        "statement_descriptor",
        String,
        comment="Extra information about a top-up. This will appear on your source's bank statement. It must contain at least one letter",
        nullable=True,
    ),
    Column(
        "status",
        String,
        comment="The status of the top-up is either `canceled`, `failed`, `pending`, `reversed`, or `succeeded`",
    ),
    Column(
        "transfer_group",
        String,
        comment="A string that identifies this top-up as part of a group",
        nullable=True,
    ),
)
__all__ = ["topup.json"]
