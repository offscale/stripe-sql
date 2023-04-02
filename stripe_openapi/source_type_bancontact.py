from sqlalchemy import Column, String, Table

from . import metadata

SourceTypeBancontactJson = Table(
    "source_type_bancontactjson",
    metadata,
    Column("bank_code", String, nullable=True),
    Column("bank_name", String, nullable=True, primary_key=True),
    Column("bic", String, nullable=True),
    Column("iban_last4", String, nullable=True),
    Column("preferred_language", String, nullable=True),
    Column("statement_descriptor", String, nullable=True),
)
__all__ = ["source_type_bancontact.json"]
