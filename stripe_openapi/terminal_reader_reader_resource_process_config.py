from sqlalchemy import Boolean, Column, ForeignKey, Identity, Integer, Table

from . import metadata

TerminalReaderReaderResourceProcessConfig.Json = Table(
    "terminal_reader_reader_resource_process_config.json",
    metadata,
    Column(
        "skip_tipping",
        Boolean,
        comment="Override showing a tipping selection screen on this transaction",
        nullable=True,
    ),
    Column(
        "tipping",
        TerminalReaderReaderResourceTippingConfig,
        ForeignKey("TerminalReaderReaderResourceTippingConfig"),
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["terminal_reader_reader_resource_process_config.json"]
