from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

SourceTypeSepaDebit.Json = Table(
    "source_type_sepa_debit.json",
    metadata,
    Column("bank_code", String, nullable=True),
    Column("branch_code", String, nullable=True),
    Column("country", String, nullable=True),
    Column("fingerprint", String, nullable=True),
    Column("last4", String, nullable=True),
    Column("mandate_reference", String, nullable=True),
    Column("mandate_url", String, nullable=True),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["source_type_sepa_debit.json"]
