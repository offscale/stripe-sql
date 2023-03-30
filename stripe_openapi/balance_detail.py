from sqlalchemy import Column, Identity, Integer, Table, list

from . import metadata

BalanceDetail.Json = Table(
    "balance_detail.json",
    metadata,
    Column("available", list, comment="Funds that are available for use"),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["balance_detail.json"]
