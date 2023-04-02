from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

SourceTypeAlipayJson = Table(
    "source_type_alipayjson",
    metadata,
    Column("data_string", String, nullable=True),
    Column("native_url", String, nullable=True),
    Column("statement_descriptor", String, nullable=True),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["source_type_alipay.json"]
