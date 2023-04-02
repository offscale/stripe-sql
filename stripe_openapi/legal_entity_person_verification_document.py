from sqlalchemy import Column, ForeignKey, Identity, Integer, String, Table

from stripe_openapi.file import File

from . import metadata

LegalEntityPersonVerificationDocumentJson = Table(
    "legal_entity_person_verification_documentjson",
    metadata,
    Column(
        "back",
        File,
        ForeignKey("File"),
        comment="The back of an ID returned by a [file upload](https://stripe.com/docs/api#create_file) with a `purpose` value of `identity_document`",
        nullable=True,
    ),
    Column(
        "details",
        String,
        comment='A user-displayable string describing the verification state of this document. For example, if a document is uploaded and the picture is too fuzzy, this may say "Identity document is too unclear to read"',
        nullable=True,
    ),
    Column(
        "details_code",
        String,
        comment="One of `document_corrupt`, `document_country_not_supported`, `document_expired`, `document_failed_copy`, `document_failed_other`, `document_failed_test_mode`, `document_fraudulent`, `document_failed_greyscale`, `document_incomplete`, `document_invalid`, `document_manipulated`, `document_missing_back`, `document_missing_front`, `document_not_readable`, `document_not_uploaded`, `document_photo_mismatch`, `document_too_large`, or `document_type_not_supported`. A machine-readable code specifying the verification state for this document",
        nullable=True,
    ),
    Column(
        "front",
        File,
        ForeignKey("File"),
        comment="The front of an ID returned by a [file upload](https://stripe.com/docs/api#create_file) with a `purpose` value of `identity_document`",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["legal_entity_person_verification_document.json"]
