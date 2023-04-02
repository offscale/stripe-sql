from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

SourceMandateNotificationBacsDebitDataJson = Table(
    "source_mandate_notification_bacs_debit_datajson",
    metadata,
    Column(
        "last4",
        String,
        comment="Last 4 digits of the account number associated with the debit",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["source_mandate_notification_bacs_debit_data.json"]
