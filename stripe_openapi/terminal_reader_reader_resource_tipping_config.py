from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

TerminalReaderReaderResourceTippingConfig.Json = Table(
    "terminal_reader_reader_resource_tipping_config.json",
    metadata,
    Column(
        "amount_eligible",
        Integer,
        comment="Amount used to calculate tip suggestions on tipping selection screen for this transaction. Must be a positive integer in the smallest currency unit (e.g., 100 cents to represent $1.00 or 100 to represent ¥100, a zero-decimal currency)",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["terminal_reader_reader_resource_tipping_config.json"]
