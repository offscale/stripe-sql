from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

SourceTypeCardPresentJson = Table(
    "source_type_card_presentjson",
    metadata,
    Column("application_cryptogram", String, nullable=True),
    Column("application_preferred_name", String, nullable=True),
    Column("authorization_code", String, nullable=True),
    Column("authorization_response_code", String, nullable=True),
    Column("brand", String, nullable=True),
    Column("country", String, nullable=True),
    Column("cvm_type", String, nullable=True),
    Column("data_type", String, nullable=True),
    Column("dedicated_file_name", String, nullable=True),
    Column("description", String, nullable=True),
    Column("emv_auth_data", String, nullable=True),
    Column("evidence_customer_signature", String, nullable=True),
    Column("evidence_transaction_certificate", String, nullable=True),
    Column("exp_month", Integer, nullable=True),
    Column("exp_year", Integer, nullable=True),
    Column("fingerprint", String, nullable=True),
    Column("funding", String, nullable=True),
    Column("iin", String, nullable=True),
    Column("issuer", String, nullable=True),
    Column("last4", String, nullable=True),
    Column("pos_device_id", String, nullable=True),
    Column("pos_entry_mode", String, nullable=True),
    Column("read_method", String, nullable=True),
    Column("reader", String, nullable=True),
    Column("terminal_verification_results", String, nullable=True),
    Column("transaction_status_information", String, nullable=True),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["source_type_card_present.json"]
