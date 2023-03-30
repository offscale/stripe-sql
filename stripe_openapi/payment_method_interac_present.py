from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

PaymentMethodInteracPresent.Json = Table(
    "payment_method_interac_present.json",
    metadata,
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_method_interac_present.json"]
