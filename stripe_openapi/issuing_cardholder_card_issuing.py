from sqlalchemy import Column, ForeignKey, Identity, Integer, Table

from . import metadata

IssuingCardholderCardIssuing.Json = Table(
    "issuing_cardholder_card_issuing.json",
    metadata,
    Column(
        "user_terms_acceptance",
        IssuingCardholderUserTermsAcceptance,
        ForeignKey("IssuingCardholderUserTermsAcceptance"),
        comment="Information about cardholder acceptance of [Authorized User Terms](https://stripe.com/docs/issuing/cards)",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["issuing_cardholder_card_issuing.json"]
