from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

PaymentMethodWechatPayJson = Table(
    "payment_method_wechat_payjson",
    metadata,
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_method_wechat_pay.json"]
