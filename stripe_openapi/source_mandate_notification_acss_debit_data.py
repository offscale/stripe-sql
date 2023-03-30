from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

SourceMandateNotificationAcssDebitData.Json = Table(
    "source_mandate_notification_acss_debit_data.json",
    metadata,
    Column(
        "statement_descriptor",
        String,
        comment="The statement descriptor associate with the debit",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["source_mandate_notification_acss_debit_data.json"]
