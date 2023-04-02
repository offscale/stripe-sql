from sqlalchemy import Column, String, Table

from . import metadata

TaxIdVerificationJson = Table(
    "tax_id_verificationjson",
    metadata,
    Column(
        "status",
        String,
        comment="Verification status, one of `pending`, `verified`, `unverified`, or `unavailable`",
    ),
    Column("verified_address", String, comment="Verified address", nullable=True),
    Column(
        "verified_name",
        String,
        comment="Verified name",
        nullable=True,
        primary_key=True,
    ),
)
__all__ = ["tax_id_verification.json"]
