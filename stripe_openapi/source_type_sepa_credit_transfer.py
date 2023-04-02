from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

SourceTypeSepaCreditTransferJson = Table(
    "source_type_sepa_credit_transferjson",
    metadata,
    Column("bank_name", String, nullable=True),
    Column("bic", String, nullable=True),
    Column("iban", String, nullable=True),
    Column("refund_account_holder_address_city", String, nullable=True),
    Column("refund_account_holder_address_country", String, nullable=True),
    Column("refund_account_holder_address_line1", String, nullable=True),
    Column("refund_account_holder_address_line2", String, nullable=True),
    Column("refund_account_holder_address_postal_code", String, nullable=True),
    Column("refund_account_holder_address_state", String, nullable=True),
    Column("refund_account_holder_name", String, nullable=True),
    Column("refund_iban", String, nullable=True),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["source_type_sepa_credit_transfer.json"]
