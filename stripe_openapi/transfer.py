from sqlalchemy import JSON, Boolean, Column, ForeignKey, Integer, String, Table

from stripe_openapi.account import Account
from stripe_openapi.charge import Charge

from . import metadata

TransferJson = Table(
    "transferjson",
    metadata,
    Column("amount", Integer, comment="Amount in %s to be transferred"),
    Column(
        "amount_reversed",
        Integer,
        comment="Amount in %s reversed (can be less than the amount attribute on the transfer if a partial reversal was issued)",
    ),
    Column(
        "balance_transaction",
        BalanceTransaction,
        ForeignKey("BalanceTransaction"),
        comment="Balance transaction that describes the impact of this transfer on your account balance",
        nullable=True,
    ),
    Column(
        "created",
        Integer,
        comment="Time that this record of the transfer was first created",
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
        "destination",
        Account,
        ForeignKey("Account"),
        comment="ID of the Stripe account the transfer was sent to",
        nullable=True,
    ),
    Column(
        "destination_payment",
        Charge,
        ForeignKey("Charge"),
        comment="If the destination is a Stripe account, this will be the ID of the payment that the destination account received for the transfer",
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
        "reversals",
        JSON,
        comment="A list of reversals that have been applied to the transfer",
    ),
    Column(
        "reversed",
        Boolean,
        comment="Whether the transfer has been fully reversed. If the transfer is only partially reversed, this attribute will still be false",
    ),
    Column(
        "source_transaction",
        Charge,
        ForeignKey("Charge"),
        comment="ID of the charge or payment that was used to fund the transfer. If null, the transfer was funded from the available balance",
        nullable=True,
    ),
    Column(
        "source_type",
        String,
        comment="The source balance this transfer came from. One of `card`, `fpx`, or `bank_account`",
        nullable=True,
    ),
    Column(
        "transfer_group",
        String,
        comment="A string that identifies this transaction as part of a group. See the [Connect documentation](https://stripe.com/docs/connect/charges-transfers#transfer-options) for details",
        nullable=True,
    ),
)
__all__ = ["transfer.json"]
