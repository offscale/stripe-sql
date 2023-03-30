from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

MandateMultiUse.Json = Table(
    "mandate_multi_use.json",
    metadata,
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["mandate_multi_use.json"]
