from sqlalchemy import Column, ForeignKey, Integer, String, Table, list

from stripe_openapi.price import Price

from . import metadata

Item.Json = Table(
    "item.json",
    metadata,
    Column(
        "amount_discount",
        Integer,
        comment="Total discount amount applied. If no discounts were applied, defaults to 0",
    ),
    Column(
        "amount_subtotal",
        Integer,
        comment="Total before any discounts or taxes are applied",
    ),
    Column(
        "amount_tax",
        Integer,
        comment="Total tax amount applied. If no tax was applied, defaults to 0",
    ),
    Column("amount_total", Integer, comment="Total after discounts and taxes"),
    Column(
        "currency",
        String,
        comment="Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)",
    ),
    Column(
        "description",
        String,
        comment="An arbitrary string attached to the object. Often useful for displaying to users. Defaults to product name",
    ),
    Column(
        "discounts",
        list,
        comment="The discounts applied to the line item",
        nullable=True,
    ),
    Column("id", String, comment="Unique identifier for the object", primary_key=True),
    Column(
        "object",
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    ),
    Column(
        "price",
        Price,
        ForeignKey("Price"),
        comment="The price used to generate the line item",
        nullable=True,
    ),
    Column(
        "quantity",
        Integer,
        comment="The quantity of products being purchased",
        nullable=True,
    ),
    Column("taxes", list, comment="The taxes applied to the line item", nullable=True),
)
__all__ = ["item.json"]
