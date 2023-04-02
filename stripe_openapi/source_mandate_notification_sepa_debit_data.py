from sqlalchemy import Column, String, Table

from . import metadata

SourceMandateNotificationSepaDebitDataJson = Table(
    "source_mandate_notification_sepa_debit_datajson",
    metadata,
    Column(
        "creditor_identifier",
        String,
        comment="SEPA creditor ID",
        nullable=True,
        primary_key=True,
    ),
    Column(
        "last4",
        String,
        comment="Last 4 digits of the account number associated with the debit",
        nullable=True,
    ),
    Column(
        "mandate_reference",
        String,
        comment="Mandate reference associated with the debit",
        nullable=True,
    ),
)
__all__ = ["source_mandate_notification_sepa_debit_data.json"]
