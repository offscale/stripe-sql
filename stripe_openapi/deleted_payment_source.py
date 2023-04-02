from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

DeletedPaymentSourceJson = Table(
    "deleted_payment_sourcejson",
    metadata,
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["deleted_payment_source.json"]
