from sqlalchemy import Column, String, Table

from . import metadata

PaymentMethodDetailsWechatPayJson = Table(
    "payment_method_details_wechat_payjson",
    metadata,
    Column(
        "fingerprint",
        String,
        comment="Uniquely identifies this particular WeChat Pay account. You can use this attribute to check whether two WeChat accounts are the same",
        nullable=True,
    ),
    Column(
        "transaction_id",
        String,
        comment="Transaction ID of this particular WeChat Pay transaction",
        nullable=True,
        primary_key=True,
    ),
)
__all__ = ["payment_method_details_wechat_pay.json"]
