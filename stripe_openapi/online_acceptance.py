from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

OnlineAcceptance.Json = Table(
    "online_acceptance.json",
    metadata,
    Column(
        "ip_address",
        String,
        comment="The IP address from which the Mandate was accepted by the customer",
        nullable=True,
    ),
    Column(
        "user_agent",
        String,
        comment="The user agent of the browser from which the Mandate was accepted by the customer",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["online_acceptance.json"]
