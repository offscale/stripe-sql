from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

PaymentMethodBancontactJson = Table(
    "payment_method_bancontactjson",
    metadata,
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_method_bancontact.json"]
