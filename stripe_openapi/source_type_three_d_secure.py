from sqlalchemy import Boolean, Column, Identity, Integer, String, Table

from . import metadata

SourceTypeThreeDSecure.Json = Table(
    "source_type_three_d_secure.json",
    metadata,
    Column("address_line1_check", String, nullable=True),
    Column("address_zip_check", String, nullable=True),
    Column("authenticated", Boolean, nullable=True),
    Column("brand", String, nullable=True),
    Column("card", String, nullable=True),
    Column("country", String, nullable=True),
    Column("customer", String, nullable=True),
    Column("cvc_check", String, nullable=True),
    Column("description", String, nullable=True),
    Column("dynamic_last4", String, nullable=True),
    Column("exp_month", Integer, nullable=True),
    Column("exp_year", Integer, nullable=True),
    Column("fingerprint", String, nullable=True),
    Column("funding", String, nullable=True),
    Column("iin", String, nullable=True),
    Column("issuer", String, nullable=True),
    Column("last4", String, nullable=True),
    Column("name", String, nullable=True),
    Column("three_d_secure", String, nullable=True),
    Column("tokenization_method", String, nullable=True),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["source_type_three_d_secure.json"]
