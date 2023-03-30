from sqlalchemy import JSON, Boolean, Column, ForeignKey, Integer, String, Table

from stripe_openapi.account import Account
from stripe_openapi.application import Application
from stripe_openapi.charge import Charge

from . import metadata

ApplicationFee.Json = Table(
    "application_fee.json",
    metadata,
    Column(
        "account",
        Account,
        ForeignKey("Account"),
        comment="ID of the Stripe account this fee was taken from",
    ),
    Column("amount", Integer, comment="Amount earned, in %s"),
    Column(
        "amount_refunded",
        Integer,
        comment="Amount in %s refunded (can be less than the amount attribute on the fee if a partial refund was issued)",
    ),
    Column(
        "application",
        Application,
        ForeignKey("Application"),
        comment="ID of the Connect application that earned the fee",
    ),
    Column(
        "balance_transaction",
        BalanceTransaction,
        ForeignKey("BalanceTransaction"),
        comment="Balance transaction that describes the impact of this collected application fee on your account balance (not including refunds)",
        nullable=True,
    ),
    Column(
        "charge",
        Charge,
        ForeignKey("Charge"),
        comment="ID of the charge that the application fee was taken from",
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
    Column(
        "originating_transaction",
        Charge,
        ForeignKey("Charge"),
        comment="ID of the corresponding charge on the platform account, if this fee was the result of a charge using the `destination` parameter",
        nullable=True,
    ),
    Column(
        "refunded",
        Boolean,
        comment="Whether the fee has been fully refunded. If the fee is only partially refunded, this attribute will still be false",
    ),
    Column(
        "refunds", JSON, comment="A list of refunds that have been applied to the fee"
    ),
)
__all__ = ["application_fee.json"]
