from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

SourceTypeAuBecsDebitJson = Table(
    "source_type_au_becs_debitjson",
    metadata,
    Column("bsb_number", String, nullable=True),
    Column("fingerprint", String, nullable=True),
    Column("last4", String, nullable=True),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["source_type_au_becs_debit.json"]
