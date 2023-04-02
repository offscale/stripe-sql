from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

SourceTransactionPaperCheckDataJson = Table(
    "source_transaction_paper_check_datajson",
    metadata,
    Column(
        "available_at",
        String,
        comment="Time at which the deposited funds will be available for use. Measured in seconds since the Unix epoch",
        nullable=True,
    ),
    Column(
        "invoices",
        String,
        comment="Comma-separated list of invoice IDs associated with the paper check",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["source_transaction_paper_check_data.json"]
