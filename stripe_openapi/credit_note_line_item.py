from sqlalchemy import Boolean, Column, Integer, String, Table, list

from . import metadata

CreditNoteLineItemJson = Table(
    "credit_note_line_itemjson",
    metadata,
    Column(
        "amount",
        Integer,
        comment="The integer amount in %s representing the gross amount being credited for this line item, excluding (exclusive) tax and discounts",
    ),
    Column(
        "amount_excluding_tax",
        Integer,
        comment="The integer amount in %s representing the amount being credited for this line item, excluding all tax and discounts",
        nullable=True,
    ),
    Column(
        "description",
        String,
        comment="Description of the item being credited",
        nullable=True,
    ),
    Column(
        "discount_amount",
        Integer,
        comment="The integer amount in %s representing the discount being credited for this line item",
    ),
    Column(
        "discount_amounts",
        list,
        comment="The amount of discount calculated per discount for this line item",
    ),
    Column("id", String, comment="Unique identifier for the object", primary_key=True),
    Column(
        "invoice_line_item",
        String,
        comment="ID of the invoice line item being credited",
        nullable=True,
    ),
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
        "quantity",
        Integer,
        comment="The number of units of product being credited",
        nullable=True,
    ),
    Column(
        "tax_amounts",
        list,
        comment="The amount of tax calculated per tax rate for this line item",
    ),
    Column("tax_rates", list, comment="The tax rates which apply to the line item"),
    Column(
        "type",
        String,
        comment="The type of the credit note line item, one of `invoice_line_item` or `custom_line_item`. When the type is `invoice_line_item` there is an additional `invoice_line_item` property on the resource the value of which is the id of the credited line item on the invoice",
    ),
    Column(
        "unit_amount",
        Integer,
        comment="The cost of each unit of product being credited",
        nullable=True,
    ),
    Column(
        "unit_amount_decimal",
        String,
        comment="Same as `unit_amount`, but contains a decimal value with at most 12 decimal places",
        nullable=True,
    ),
    Column(
        "unit_amount_excluding_tax",
        String,
        comment="The amount in %s representing the unit amount being credited for this line item, excluding all tax and discounts",
        nullable=True,
    ),
)
__all__ = ["credit_note_line_item.json"]
