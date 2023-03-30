from sqlalchemy import Column, ForeignKey, Identity, Integer, String, Table

from stripe_openapi.file import File

from . import metadata

LegalEntityCompanyVerificationDocument.Json = Table(
    "legal_entity_company_verification_document.json",
    metadata,
    Column(
        "back",
        File,
        ForeignKey("File"),
        comment="The back of a document returned by a [file upload](https://stripe.com/docs/api#create_file) with a `purpose` value of `additional_verification`",
        nullable=True,
    ),
    Column(
        "details",
        String,
        comment="A user-displayable string describing the verification state of this document",
        nullable=True,
    ),
    Column(
        "details_code",
        String,
        comment="One of `document_corrupt`, `document_expired`, `document_failed_copy`, `document_failed_greyscale`, `document_failed_other`, `document_failed_test_mode`, `document_fraudulent`, `document_incomplete`, `document_invalid`, `document_manipulated`, `document_not_readable`, `document_not_uploaded`, `document_type_not_supported`, or `document_too_large`. A machine-readable code specifying the verification state for this document",
        nullable=True,
    ),
    Column(
        "front",
        File,
        ForeignKey("File"),
        comment="The front of a document returned by a [file upload](https://stripe.com/docs/api#create_file) with a `purpose` value of `additional_verification`",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["legal_entity_company_verification_document.json"]
