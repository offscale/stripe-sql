from sqlalchemy import Column, String, Table

from . import metadata

SourceTypeGiropay.Json = Table(
    "source_type_giropay.json",
    metadata,
    Column("bank_code", String, nullable=True),
    Column("bank_name", String, nullable=True, primary_key=True),
    Column("bic", String, nullable=True),
    Column("statement_descriptor", String, nullable=True),
)
__all__ = ["source_type_giropay.json"]
