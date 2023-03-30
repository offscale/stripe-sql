from sqlalchemy import Column, ForeignKey, Identity, Integer, String, Table

from . import metadata

CustomerAcceptance.Json = Table(
    "customer_acceptance.json",
    metadata,
    Column(
        "accepted_at",
        Integer,
        comment="The time at which the customer accepted the Mandate",
        nullable=True,
    ),
    Column(
        "offline", OfflineAcceptance, ForeignKey("OfflineAcceptance"), nullable=True
    ),
    Column("online", OnlineAcceptance, ForeignKey("OnlineAcceptance"), nullable=True),
    Column(
        "type",
        String,
        comment="The type of customer acceptance information included with the Mandate. One of `online` or `offline`",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["customer_acceptance.json"]
