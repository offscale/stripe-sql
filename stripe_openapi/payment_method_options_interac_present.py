from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

PaymentMethodOptionsInteracPresentJson = Table(
    "payment_method_options_interac_presentjson",
    metadata,
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_method_options_interac_present.json"]
