from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

DeletedExternalAccountJson = Table(
    "deleted_external_accountjson",
    metadata,
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["deleted_external_account.json"]
