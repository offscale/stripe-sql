from sqlalchemy import Column, ForeignKey, Identity, Integer, String, Table

from stripe_openapi.file import File

from . import metadata

IssuingDisputeServiceNotAsDescribedEvidenceJson = Table(
    "issuing_dispute_service_not_as_described_evidencejson",
    metadata,
    Column(
        "additional_documentation",
        File,
        ForeignKey("File"),
        comment="(ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Additional documentation supporting the dispute",
        nullable=True,
    ),
    Column(
        "canceled_at", Integer, comment="Date when order was canceled", nullable=True
    ),
    Column(
        "cancellation_reason",
        String,
        comment="Reason for canceling the order",
        nullable=True,
    ),
    Column(
        "explanation",
        String,
        comment="Explanation of why the cardholder is disputing this transaction",
        nullable=True,
    ),
    Column(
        "received_at",
        Integer,
        comment="Date when the product was received",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["issuing_dispute_service_not_as_described_evidence.json"]
