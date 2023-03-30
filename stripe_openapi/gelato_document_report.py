from sqlalchemy import ARRAY, Column, ForeignKey, Identity, Integer, String, Table

from stripe_openapi.address import Address

from . import metadata

GelatoDocumentReport.Json = Table(
    "gelato_document_report.json",
    metadata,
    Column(
        "address",
        Address,
        ForeignKey("Address"),
        comment="Address as it appears in the document",
        nullable=True,
    ),
    Column(
        "dob",
        GelatoDataDocumentReportDateOfBirth,
        ForeignKey("GelatoDataDocumentReportDateOfBirth"),
        comment="Date of birth as it appears in the document",
        nullable=True,
    ),
    Column(
        "error",
        GelatoDocumentReportError,
        ForeignKey("GelatoDocumentReportError"),
        comment="Details on the verification error. Present when status is `unverified`",
        nullable=True,
    ),
    Column(
        "expiration_date",
        GelatoDataDocumentReportExpirationDate,
        ForeignKey("GelatoDataDocumentReportExpirationDate"),
        comment="Expiration date of the document",
        nullable=True,
    ),
    Column(
        "files",
        ARRAY(String),
        comment="Array of [File](https://stripe.com/docs/api/files) ids containing images for this document",
        nullable=True,
    ),
    Column(
        "first_name",
        String,
        comment="First name as it appears in the document",
        nullable=True,
    ),
    Column(
        "issued_date",
        GelatoDataDocumentReportIssuedDate,
        ForeignKey("GelatoDataDocumentReportIssuedDate"),
        comment="Issued date of the document",
        nullable=True,
    ),
    Column(
        "issuing_country",
        String,
        comment="Issuing country of the document",
        nullable=True,
    ),
    Column(
        "last_name",
        String,
        comment="Last name as it appears in the document",
        nullable=True,
    ),
    Column("number", String, comment="Document ID number", nullable=True),
    Column("status", String, comment="Status of this `document` check"),
    Column("type", String, comment="Type of the document", nullable=True),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["gelato_document_report.json"]
