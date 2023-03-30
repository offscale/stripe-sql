from sqlalchemy import Column, ForeignKey, Identity, Integer, Table

from . import metadata

IssuingCardholderVerification.Json = Table(
    "issuing_cardholder_verification.json",
    metadata,
    Column(
        "document",
        IssuingCardholderIdDocument,
        ForeignKey("IssuingCardholderIdDocument"),
        comment="An identifying document, either a passport or local ID card",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["issuing_cardholder_verification.json"]
