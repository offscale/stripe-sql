from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

BalanceAmountBySourceType.Json = Table(
    "balance_amount_by_source_type.json",
    metadata,
    Column("bank_account", Integer, comment="Amount for bank account", nullable=True),
    Column("card", Integer, comment="Amount for card", nullable=True),
    Column("fpx", Integer, comment="Amount for FPX", nullable=True),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["balance_amount_by_source_type.json"]
