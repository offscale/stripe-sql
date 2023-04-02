from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

BalanceTransactionSourceJson = Table(
    "balance_transaction_sourcejson",
    metadata,
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["balance_transaction_source.json"]
