from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

SourceTypeP24.Json = Table(
    "source_type_p24.json",
    metadata,
    Column("reference", String, nullable=True),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["source_type_p24.json"]
