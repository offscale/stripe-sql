from sqlalchemy import Column, ForeignKey, Identity, Integer, String, Table

from . import metadata

TerminalReaderReaderResourceSetReaderDisplayAction.Json = Table(
    "terminal_reader_reader_resource_set_reader_display_action.json",
    metadata,
    Column(
        "cart",
        TerminalReaderReaderResourceCart,
        ForeignKey("TerminalReaderReaderResourceCart"),
        comment="Cart object to be displayed by the reader",
        nullable=True,
    ),
    Column("type", String, comment="Type of information to be displayed by the reader"),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["terminal_reader_reader_resource_set_reader_display_action.json"]
