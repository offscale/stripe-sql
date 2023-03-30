from sqlalchemy import Column, ForeignKey, Identity, Integer, String, Table

from . import metadata

LegalEntityPersonVerification.Json = Table(
    "legal_entity_person_verification.json",
    metadata,
    Column(
        "additional_document",
        LegalEntityPersonVerificationDocument,
        ForeignKey("LegalEntityPersonVerificationDocument"),
        comment="A document showing address, either a passport, local ID card, or utility bill from a well-known utility company",
        nullable=True,
    ),
    Column(
        "details",
        String,
        comment='A user-displayable string describing the verification state for the person. For example, this may say "Provided identity information could not be verified"',
        nullable=True,
    ),
    Column(
        "details_code",
        String,
        comment="One of `document_address_mismatch`, `document_dob_mismatch`, `document_duplicate_type`, `document_id_number_mismatch`, `document_name_mismatch`, `document_nationality_mismatch`, `failed_keyed_identity`, or `failed_other`. A machine-readable code specifying the verification state for the person",
        nullable=True,
    ),
    Column(
        "document",
        LegalEntityPersonVerificationDocument,
        ForeignKey("LegalEntityPersonVerificationDocument"),
        nullable=True,
    ),
    Column(
        "status",
        String,
        comment="The state of verification for the person. Possible values are `unverified`, `pending`, or `verified`",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["legal_entity_person_verification.json"]
