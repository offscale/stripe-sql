from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

PaymentMethodDetailsWechat.Json = Table(
    "payment_method_details_wechat.json",
    metadata,
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_method_details_wechat.json"]
