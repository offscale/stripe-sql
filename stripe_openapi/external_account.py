from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

ExternalAccountJson = Table(
    "external_accountjson",
    metadata,
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["external_account.json"]
