from sqlalchemy import Boolean, Column, Identity, Integer, String, Table

from . import metadata

IssuingCardApplePay.Json = Table(
    "issuing_card_apple_pay.json",
    metadata,
    Column("eligible", Boolean, comment="Apple Pay Eligibility"),
    Column(
        "ineligible_reason",
        String,
        comment="Reason the card is ineligible for Apple Pay",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["issuing_card_apple_pay.json"]
