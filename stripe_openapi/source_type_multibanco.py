from sqlalchemy import Column, String, Table

from . import metadata

SourceTypeMultibancoJson = Table(
    "source_type_multibancojson",
    metadata,
    Column("entity", String, nullable=True),
    Column("reference", String, nullable=True),
    Column("refund_account_holder_address_city", String, nullable=True),
    Column("refund_account_holder_address_country", String, nullable=True),
    Column("refund_account_holder_address_line1", String, nullable=True),
    Column("refund_account_holder_address_line2", String, nullable=True),
    Column("refund_account_holder_address_postal_code", String, nullable=True),
    Column("refund_account_holder_address_state", String, nullable=True),
    Column("refund_account_holder_name", String, nullable=True, primary_key=True),
    Column("refund_iban", String, nullable=True),
)
__all__ = ["source_type_multibanco.json"]
