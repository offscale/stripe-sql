from sqlalchemy import Column, ForeignKey, Identity, Integer, String, Table

from stripe_openapi.file import File

from . import metadata

IssuingDisputeMerchandiseNotAsDescribedEvidenceJson = Table(
    "issuing_dispute_merchandise_not_as_described_evidencejson",
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
    Column(
        "received_at",
        Integer,
        comment="Date when the product was received",
        nullable=True,
    ),
    Column(
        "return_description",
        String,
        comment="Description of the cardholder's attempt to return the product",
        nullable=True,
    ),
    Column(
        "return_status",
        String,
        comment="Result of cardholder's attempt to return the product",
        nullable=True,
    ),
    Column(
        "returned_at",
        Integer,
        comment="Date when the product was returned or attempted to be returned",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["issuing_dispute_merchandise_not_as_described_evidence.json"]
