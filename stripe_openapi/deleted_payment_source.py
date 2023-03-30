from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

DeletedPaymentSource.Json = Table(
    "deleted_payment_source.json",
    metadata,
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["deleted_payment_source.json"]
