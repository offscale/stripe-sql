from sqlalchemy import JSON, Boolean, Column, ForeignKey, Integer, String, Table, list

from stripe_openapi.plan import Plan
from stripe_openapi.price import Price

from . import metadata

LineItemJson = Table(
    "line_itemjson",
    metadata,
    Column("amount", Integer, comment="The amount, in %s"),
    Column(
        "amount_excluding_tax",
        Integer,
        comment="The integer amount in %s representing the amount for this line item, excluding all tax and discounts",
        nullable=True,
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
        "discount_amounts",
        list,
        comment="The amount of discount calculated per discount for this line item",
        nullable=True,
    ),
    Column(
        "discountable",
        Boolean,
        comment="If true, discounts will apply to this line item. Always false for prorations",
    ),
    Column(
        "discounts",
        list,
        comment="The discounts applied to the invoice line item. Line item discounts are applied before invoice discounts. Use `expand[]=discounts` to expand each discount",
        nullable=True,
    ),
    Column("id", String, comment="Unique identifier for the object", primary_key=True),
    Column(
        "invoice_item",
        String,
        comment="The ID of the [invoice item](https://stripe.com/docs/api/invoiceitems) associated with this line item if any",
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
        comment="Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Note that for line items with `type=subscription` this will reflect the metadata of the subscription that caused the line item to be created",
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
        comment="The plan of the subscription, if the line item is a subscription or a proration",
        nullable=True,
    ),
    Column(
        "price",
        Price,
        ForeignKey("Price"),
        comment="The price of the line item",
        nullable=True,
    ),
    Column("proration", Boolean, comment="Whether this is a proration"),
    Column(
        "proration_details",
        InvoicesLineItemsProrationDetails,
        ForeignKey("InvoicesLineItemsProrationDetails"),
        comment="Additional details for proration line items",
        nullable=True,
    ),
    Column(
        "quantity",
        Integer,
        comment="The quantity of the subscription, if the line item is a subscription or a proration",
        nullable=True,
    ),
    Column(
        "subscription",
        String,
        comment="The subscription that the invoice item pertains to, if any",
        nullable=True,
    ),
    Column(
        "subscription_item",
        String,
        comment="The subscription item that generated this line item. Left empty if the line item is not an explicit result of a subscription",
        nullable=True,
    ),
    Column(
        "tax_amounts",
        list,
        comment="The amount of tax calculated per tax rate for this line item",
        nullable=True,
    ),
    Column(
        "tax_rates",
        list,
        comment="The tax rates which apply to the line item",
        nullable=True,
    ),
    Column(
        "type",
        String,
        comment="A string identifying the type of the source of this line item, either an `invoiceitem` or a `subscription`",
    ),
    Column(
        "unit_amount_excluding_tax",
        String,
        comment="The amount in %s representing the unit amount for this line item, excluding all tax and discounts",
        nullable=True,
    ),
)
__all__ = ["line_item.json"]
