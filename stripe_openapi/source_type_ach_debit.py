from sqlalchemy import Column, String, Table

from . import metadata

SourceTypeAchDebitJson = Table(
    "source_type_ach_debitjson",
    metadata,
    Column("bank_name", String, nullable=True, primary_key=True),
    Column("country", String, nullable=True),
    Column("fingerprint", String, nullable=True),
    Column("last4", String, nullable=True),
    Column("routing_number", String, nullable=True),
    Column("type", String, nullable=True),
)
__all__ = ["source_type_ach_debit.json"]
