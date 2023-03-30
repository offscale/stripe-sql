from sqlalchemy import Column, ForeignKey, Identity, Integer, Table

from . import metadata

Error.Json = Table(
    "error.json",
    metadata,
    Column("error", ApiErrors, ForeignKey("ApiErrors")),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["error.json"]
