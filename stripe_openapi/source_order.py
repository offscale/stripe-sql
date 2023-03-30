from sqlalchemy import Column, ForeignKey, Identity, Integer, String, Table, list

from stripe_openapi.shipping import Shipping

from . import metadata

SourceOrder.Json = Table(
    "source_order.json",
    metadata,
    Column(
        "amount",
        Integer,
        comment="A positive integer in the smallest currency unit (that is, 100 cents for $1.00, or 1 for ¥1, Japanese Yen being a zero-decimal currency) representing the total amount for the order",
    ),
    Column(
        "currency",
        String,
        comment="Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)",
    ),
    Column(
        "email",
        String,
        comment="The email address of the customer placing the order",
        nullable=True,
    ),
    Column(
        "items", list, comment="List of items constituting the order", nullable=True
    ),
    Column("shipping", Shipping, ForeignKey("Shipping"), nullable=True),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["source_order.json"]
