from sqlalchemy import JSON, Boolean, Column, ForeignKey, Integer, String, Table

from stripe_openapi.customer import Customer
from stripe_openapi.invoice import Invoice

from . import metadata

CustomerBalanceTransaction.Json = Table(
    "customer_balance_transaction.json",
    metadata,
    Column(
        "amount",
        Integer,
        comment="The amount of the transaction. A negative value is a credit for the customer's balance, and a positive value is a debit to the customer's `balance`",
    ),
    Column(
        "created",
        Integer,
        comment="Time at which the object was created. Measured in seconds since the Unix epoch",
    ),
    Column(
        "credit_note",
        CreditNote,
        ForeignKey("CreditNote"),
        comment="The ID of the credit note (if any) related to the transaction",
        nullable=True,
    ),
    Column(
        "currency",
        String,
        comment="Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)",
    ),
    Column(
        "customer",
        Customer,
        ForeignKey("Customer"),
        comment="The ID of the customer the transaction belongs to",
    ),
    Column(
        "description",
        String,
        comment="An arbitrary string attached to the object. Often useful for displaying to users",
        nullable=True,
    ),
    Column(
        "ending_balance",
        Integer,
        comment="The customer's `balance` after the transaction was applied. A negative value decreases the amount due on the customer's next invoice. A positive value increases the amount due on the customer's next invoice",
    ),
    Column("id", String, comment="Unique identifier for the object", primary_key=True),
    Column(
        "invoice",
        Invoice,
        ForeignKey("Invoice"),
        comment="The ID of the invoice (if any) related to the transaction",
        nullable=True,
    ),
    Column(
        "livemode",
        Boolean,
        comment="Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode",
    ),
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
        "type",
        String,
        comment="Transaction type: `adjustment`, `applied_to_invoice`, `credit_note`, `initial`, `invoice_overpaid`, `invoice_too_large`, `invoice_too_small`, `unspent_receiver_credit`, or `unapplied_from_invoice`. See the [Customer Balance page](https://stripe.com/docs/billing/customer/balance#types) to learn more about transaction types",
    ),
)
__all__ = ["customer_balance_transaction.json"]
