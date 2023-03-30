from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

DeletedExternalAccount.Json = Table(
    "deleted_external_account.json",
    metadata,
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["deleted_external_account.json"]
