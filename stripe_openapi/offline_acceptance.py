from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

OfflineAcceptance.Json = Table(
    "offline_acceptance.json",
    metadata,
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["offline_acceptance.json"]
