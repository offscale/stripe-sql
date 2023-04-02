from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

PaymentMethodDetailsWechatJson = Table(
    "payment_method_details_wechatjson",
    metadata,
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_method_details_wechat.json"]
