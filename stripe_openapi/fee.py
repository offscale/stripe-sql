from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

FeeJson = Table(
    "feejson",
    metadata,
    Column("amount", Integer, comment="Amount of the fee, in cents"),
    Column(
        "application",
        String,
        comment="ID of the Connect application that earned the fee",
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
        "type",
        String,
        comment="Type of the fee, one of: `application_fee`, `stripe_fee` or `tax`",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["fee.json"]
