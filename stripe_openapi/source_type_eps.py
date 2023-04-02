from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

SourceTypeEpsJson = Table(
    "source_type_epsjson",
    metadata,
    Column("reference", String, nullable=True),
    Column("statement_descriptor", String, nullable=True),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["source_type_eps.json"]
