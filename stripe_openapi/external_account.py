from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

ExternalAccount.Json = Table(
    "external_account.json",
    metadata,
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["external_account.json"]
