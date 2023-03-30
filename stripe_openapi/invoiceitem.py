from sqlalchemy import JSON, Boolean, Column, ForeignKey, Integer, String, Table, list

from stripe_openapi.customer import Customer
from stripe_openapi.invoice import Invoice
from stripe_openapi.plan import Plan
from stripe_openapi.price import Price
from stripe_openapi.subscription import Subscription

from . import metadata

Invoiceitem.Json = Table(
    "invoiceitem.json",
    metadata,
    Column(
        "amount",
        Integer,
        comment="Amount (in the `currency` specified) of the invoice item. This should always be equal to `unit_amount * quantity`",
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
        comment="The ID of the customer who will be billed when this invoice item is billed",
    ),
    Column(
        "date",
        Integer,
        comment="Time at which the object was created. Measured in seconds since the Unix epoch",
    ),
    Column(
        "description",
        String,
        comment="An arbitrary string attached to the object. Often useful for displaying to users",
        nullable=True,
    ),
    Column(
        "discountable",
        Boolean,
        comment="If true, discounts will apply to this invoice item. Always false for prorations",
    ),
    Column(
        "discounts",
        list,
        comment="The discounts which apply to the invoice item. Item discounts are applied before invoice discounts. Use `expand[]=discounts` to expand each discount",
        nullable=True,
    ),
    Column("id", String, comment="Unique identifier for the object", primary_key=True),
    Column(
        "invoice",
        Invoice,
        ForeignKey("Invoice"),
        comment="The ID of the invoice this invoice item belongs to",
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
    Column("period", InvoiceLineItemPeriod, ForeignKey("InvoiceLineItemPeriod")),
    Column(
        "plan",
        Plan,
        ForeignKey("Plan"),
        comment="If the invoice item is a proration, the plan of the subscription that the proration was computed for",
        nullable=True,
    ),
    Column(
        "price",
        Price,
        ForeignKey("Price"),
        comment="The price of the invoice item",
        nullable=True,
    ),
    Column(
        "proration",
        Boolean,
        comment="Whether the invoice item was created automatically as a proration adjustment when the customer switched plans",
    ),
    Column(
        "quantity",
        Integer,
        comment="Quantity of units for the invoice item. If the invoice item is a proration, the quantity of the subscription that the proration was computed for",
    ),
    Column(
        "subscription",
        Subscription,
        ForeignKey("Subscription"),
        comment="The subscription that this invoice item has been created for, if any",
        nullable=True,
    ),
    Column(
        "subscription_item",
        String,
        comment="The subscription item that this invoice item has been created for, if any",
        nullable=True,
    ),
    Column(
        "tax_rates",
        list,
        comment="The tax rates which apply to the invoice item. When set, the `default_tax_rates` on the invoice do not apply to this invoice item",
        nullable=True,
    ),
    Column(
        "test_clock",
        Test_Helpers__TestClock,
        ForeignKey("Test_Helpers__TestClock"),
        comment="ID of the test clock this invoice item belongs to",
        nullable=True,
    ),
    Column(
        "unit_amount",
        Integer,
        comment="Unit amount (in the `currency` specified) of the invoice item",
        nullable=True,
    ),
    Column(
        "unit_amount_decimal",
        String,
        comment="Same as `unit_amount`, but contains a decimal value with at most 12 decimal places",
        nullable=True,
    ),
)
__all__ = ["invoiceitem.json"]
