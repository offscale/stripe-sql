from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

MandateLink.Json = Table(
    "mandate_link.json",
    metadata,
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["mandate_link.json"]
