from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

SourceTypeAchCreditTransfer.Json = Table(
    "source_type_ach_credit_transfer.json",
    metadata,
    Column("account_number", String, nullable=True),
    Column("bank_name", String, nullable=True),
    Column("fingerprint", String, nullable=True),
    Column("refund_account_holder_name", String, nullable=True),
    Column("refund_account_holder_type", String, nullable=True),
    Column("refund_routing_number", String, nullable=True),
    Column("routing_number", String, nullable=True),
    Column("swift_code", String, nullable=True),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["source_type_ach_credit_transfer.json"]
