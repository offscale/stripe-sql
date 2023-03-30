from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

AccountTermsOfService.Json = Table(
    "account_terms_of_service.json",
    metadata,
    Column(
        "date",
        Integer,
        comment="The Unix timestamp marking when the account representative accepted the service agreement",
        nullable=True,
    ),
    Column(
        "ip",
        String,
        comment="The IP address from which the account representative accepted the service agreement",
        nullable=True,
    ),
    Column(
        "user_agent",
        String,
        comment="The user agent of the browser from which the account representative accepted the service agreement",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["account_terms_of_service.json"]
