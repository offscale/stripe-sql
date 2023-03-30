from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

BalanceTransactionSource.Json = Table(
    "balance_transaction_source.json",
    metadata,
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["balance_transaction_source.json"]
