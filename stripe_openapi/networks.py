from sqlalchemy import ARRAY, Column, Identity, Integer, String, Table

from . import metadata

Networks.Json = Table(
    "networks.json",
    metadata,
    Column("available", ARRAY(String), comment="All available networks for the card"),
    Column(
        "preferred", String, comment="The preferred network for the card", nullable=True
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["networks.json"]
