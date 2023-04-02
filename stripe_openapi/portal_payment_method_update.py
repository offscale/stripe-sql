from sqlalchemy import Boolean, Column, Identity, Integer, Table

from . import metadata

PortalPaymentMethodUpdateJson = Table(
    "portal_payment_method_updatejson",
    metadata,
    Column("enabled", Boolean, comment="Whether the feature is enabled"),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["portal_payment_method_update.json"]
