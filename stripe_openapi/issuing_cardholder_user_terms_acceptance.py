from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

IssuingCardholderUserTermsAcceptanceJson = Table(
    "issuing_cardholder_user_terms_acceptancejson",
    metadata,
    Column(
        "date",
        Integer,
        comment="The Unix timestamp marking when the cardholder accepted the Authorized User Terms. Required for Celtic Spend Card users",
        nullable=True,
    ),
    Column(
        "ip",
        String,
        comment="The IP address from which the cardholder accepted the Authorized User Terms. Required for Celtic Spend Card users",
        nullable=True,
    ),
    Column(
        "user_agent",
        String,
        comment="The user agent of the browser from which the cardholder accepted the Authorized User Terms",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["issuing_cardholder_user_terms_acceptance.json"]
