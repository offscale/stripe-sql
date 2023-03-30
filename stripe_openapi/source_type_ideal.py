from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

SourceTypeIdeal.Json = Table(
    "source_type_ideal.json",
    metadata,
    Column("bank", String, nullable=True),
    Column("bic", String, nullable=True),
    Column("iban_last4", String, nullable=True),
    Column("statement_descriptor", String, nullable=True),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["source_type_ideal.json"]
