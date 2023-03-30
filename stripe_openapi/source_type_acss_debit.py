from sqlalchemy import Column, String, Table

from . import metadata

SourceTypeAcssDebit.Json = Table(
    "source_type_acss_debit.json",
    metadata,
    Column("bank_address_city", String, nullable=True),
    Column("bank_address_line_1", String, nullable=True),
    Column("bank_address_line_2", String, nullable=True),
    Column("bank_address_postal_code", String, nullable=True),
    Column("bank_name", String, nullable=True, primary_key=True),
    Column("category", String, nullable=True),
    Column("country", String, nullable=True),
    Column("fingerprint", String, nullable=True),
    Column("last4", String, nullable=True),
    Column("routing_number", String, nullable=True),
)
__all__ = ["source_type_acss_debit.json"]
