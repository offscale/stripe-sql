from sqlalchemy import Column, Identity, Integer, String, Table, list

from . import metadata

TerminalReaderReaderResourceCartJson = Table(
    "terminal_reader_reader_resource_cartjson",
    metadata,
    Column(
        "currency",
        String,
        comment="Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)",
    ),
    Column("line_items", list, comment="List of line items in the cart"),
    Column(
        "tax",
        Integer,
        comment="Tax amount for the entire cart. A positive integer in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal)",
        nullable=True,
    ),
    Column(
        "total",
        Integer,
        comment="Total amount for the entire cart, including tax. A positive integer in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal)",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["terminal_reader_reader_resource_cart.json"]
