from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

SourceTypePJson = Table(
    "source_type_pjson",
    metadata,
    Column("reference", String, nullable=True),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["source_type_p24.json"]
