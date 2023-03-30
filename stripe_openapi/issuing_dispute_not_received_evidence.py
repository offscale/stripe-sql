from sqlalchemy import Column, ForeignKey, Identity, Integer, String, Table

from stripe_openapi.file import File

from . import metadata

IssuingDisputeNotReceivedEvidence.Json = Table(
    "issuing_dispute_not_received_evidence.json",
    metadata,
    Column(
        "additional_documentation",
        File,
        ForeignKey("File"),
        comment="(ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Additional documentation supporting the dispute",
        nullable=True,
    ),
    Column(
        "expected_at",
        Integer,
        comment="Date when the cardholder expected to receive the product",
        nullable=True,
    ),
    Column(
        "explanation",
        String,
        comment="Explanation of why the cardholder is disputing this transaction",
        nullable=True,
    ),
    Column(
        "product_description",
        String,
        comment="Description of the merchandise or service that was purchased",
        nullable=True,
    ),
    Column(
        "product_type",
        String,
        comment="Whether the product was a merchandise or service",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["issuing_dispute_not_received_evidence.json"]
