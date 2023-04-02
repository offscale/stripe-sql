from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

MandateLinkJson = Table(
    "mandate_linkjson",
    metadata,
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["mandate_link.json"]
