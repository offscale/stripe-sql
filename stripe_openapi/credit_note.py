from sqlalchemy import JSON, Boolean, Column, ForeignKey, Integer, String, Table, list

from stripe_openapi.customer import Customer
from stripe_openapi.invoice import Invoice
from stripe_openapi.refund import Refund

from . import metadata

CreditNoteJson = Table(
    "credit_notejson",
    metadata,
    Column(
        "amount",
        Integer,
        comment="The integer amount in %s representing the total amount of the credit note, including tax",
    ),
    Column(
        "amount_shipping",
        Integer,
        comment="This is the sum of all the shipping amounts",
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
        "customer",
        Customer,
        ForeignKey("DeletedCustomer"),
        comment="ID of the customer",
    ),
    Column(
        "customer_balance_transaction",
        CustomerBalanceTransaction,
        ForeignKey("CustomerBalanceTransaction"),
        comment="Customer balance transaction related to this credit note",
        nullable=True,
    ),
    Column(
        "discount_amount",
        Integer,
        comment="The integer amount in %s representing the total amount of discount that was credited",
    ),
    Column(
        "discount_amounts",
        list,
        comment="The aggregate amounts calculated per discount for all line items",
    ),
    Column("id", String, comment="Unique identifier for the object", primary_key=True),
    Column("invoice", Invoice, ForeignKey("Invoice"), comment="ID of the invoice"),
    Column("lines", JSON, comment="Line items that make up the credit note"),
    Column(
        "livemode",
        Boolean,
        comment="Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode",
    ),
    Column(
        "memo",
        String,
        comment="Customer-facing text that appears on the credit note PDF",
        nullable=True,
    ),
    Column(
        "metadata",
        JSON,
        comment="Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format",
        nullable=True,
    ),
    Column(
        "number",
        String,
        comment="A unique number that identifies this particular credit note and appears on the PDF of the credit note and its associated invoice",
    ),
    Column(
        "object",
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    ),
    Column(
        "out_of_band_amount",
        Integer,
        comment="Amount that was credited outside of Stripe",
        nullable=True,
    ),
    Column("pdf", String, comment="The link to download the PDF of the credit note"),
    Column(
        "reason",
        String,
        comment="Reason for issuing this credit note, one of `duplicate`, `fraudulent`, `order_change`, or `product_unsatisfactory`",
        nullable=True,
    ),
    Column(
        "refund",
        Refund,
        ForeignKey("Refund"),
        comment="Refund related to this credit note",
        nullable=True,
    ),
    Column(
        "shipping_cost",
        InvoicesShippingCost,
        ForeignKey("InvoicesShippingCost"),
        comment="The details of the cost of shipping, including the ShippingRate applied to the invoice",
        nullable=True,
    ),
    Column(
        "status",
        String,
        comment="Status of this credit note, one of `issued` or `void`. Learn more about [voiding credit notes](https://stripe.com/docs/billing/invoices/credit-notes#voiding)",
    ),
    Column(
        "subtotal",
        Integer,
        comment="The integer amount in %s representing the amount of the credit note, excluding exclusive tax and invoice level discounts",
    ),
    Column(
        "subtotal_excluding_tax",
        Integer,
        comment="The integer amount in %s representing the amount of the credit note, excluding all tax and invoice level discounts",
        nullable=True,
    ),
    Column(
        "tax_amounts",
        list,
        comment="The aggregate amounts calculated per tax rate for all line items",
    ),
    Column(
        "total",
        Integer,
        comment="The integer amount in %s representing the total amount of the credit note, including tax and all discount",
    ),
    Column(
        "total_excluding_tax",
        Integer,
        comment="The integer amount in %s representing the total amount of the credit note, excluding tax, but including discounts",
        nullable=True,
    ),
    Column(
        "type",
        String,
        comment="Type of this credit note, one of `pre_payment` or `post_payment`. A `pre_payment` credit note means it was issued when the invoice was open. A `post_payment` credit note means it was issued when the invoice was paid",
    ),
    Column(
        "voided_at",
        Integer,
        comment="The time that the credit note was voided",
        nullable=True,
    ),
)
__all__ = ["credit_note.json"]
