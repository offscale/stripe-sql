from sqlalchemy import Column, ForeignKey, Identity, Integer, String, Table

from stripe_openapi.file import File

from . import metadata

IssuingDisputeFraudulentEvidence.Json = Table(
    "issuing_dispute_fraudulent_evidence.json",
    metadata,
    Column(
        "additional_documentation",
        File,
        ForeignKey("File"),
        comment="(ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Additional documentation supporting the dispute",
        nullable=True,
    ),
    Column(
        "explanation",
        String,
        comment="Explanation of why the cardholder is disputing this transaction",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["issuing_dispute_fraudulent_evidence.json"]
