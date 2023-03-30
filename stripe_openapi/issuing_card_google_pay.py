from sqlalchemy import Boolean, Column, Identity, Integer, String, Table

from . import metadata

IssuingCardGooglePay.Json = Table(
    "issuing_card_google_pay.json",
    metadata,
    Column("eligible", Boolean, comment="Google Pay Eligibility"),
    Column(
        "ineligible_reason",
        String,
        comment="Reason the card is ineligible for Google Pay",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["issuing_card_google_pay.json"]
