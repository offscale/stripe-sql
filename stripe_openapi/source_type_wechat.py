from sqlalchemy import Column, String, Table

from . import metadata

SourceTypeWechat.Json = Table(
    "source_type_wechat.json",
    metadata,
    Column("prepay_id", String, nullable=True, primary_key=True),
    Column("qr_code_url", String, nullable=True),
    Column("statement_descriptor", String, nullable=True),
)
__all__ = ["source_type_wechat.json"]
