from sqlalchemy import Boolean, Column, ForeignKey, Identity, Integer, String, Table

from stripe_openapi.file import File

from . import metadata

IssuingDisputeCanceledEvidence.Json = Table(
    "issuing_dispute_canceled_evidence.json",
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
        "cancellation_policy_provided",
        Boolean,
        comment="Whether the cardholder was provided with a cancellation policy",
        nullable=True,
    ),
    Column(
        "cancellation_reason",
        String,
        comment="Reason for canceling the order",
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
__all__ = ["issuing_dispute_canceled_evidence.json"]
