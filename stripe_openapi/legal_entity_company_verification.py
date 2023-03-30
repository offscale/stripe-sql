from sqlalchemy import Column, ForeignKey, Identity, Integer, Table

from . import metadata

LegalEntityCompanyVerification.Json = Table(
    "legal_entity_company_verification.json",
    metadata,
    Column(
        "document",
        LegalEntityCompanyVerificationDocument,
        ForeignKey("LegalEntityCompanyVerificationDocument"),
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["legal_entity_company_verification.json"]
