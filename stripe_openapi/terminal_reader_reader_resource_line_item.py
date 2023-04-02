from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

TerminalReaderReaderResourceLineItemJson = Table(
    "terminal_reader_reader_resource_line_itemjson",
    metadata,
    Column(
        "amount",
        Integer,
        comment="The amount of the line item. A positive integer in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal)",
    ),
    Column("description", String, comment="Description of the line item"),
    Column("quantity", Integer, comment="The quantity of the line item"),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["terminal_reader_reader_resource_line_item.json"]
