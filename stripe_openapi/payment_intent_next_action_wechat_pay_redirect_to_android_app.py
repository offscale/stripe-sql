from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

PaymentIntentNextActionWechatPayRedirectToAndroidAppJson = Table(
    "payment_intent_next_action_wechat_pay_redirect_to_android_appjson",
    metadata,
    Column(
        "app_id",
        String,
        comment="app_id is the APP ID registered on WeChat open platform",
    ),
    Column("nonce_str", String, comment="nonce_str is a random string"),
    Column("package", String, comment="package is static value"),
    Column(
        "partner_id", String, comment="an unique merchant ID assigned by WeChat Pay"
    ),
    Column("prepay_id", String, comment="an unique trading ID assigned by WeChat Pay"),
    Column("sign", String, comment="A signature"),
    Column("timestamp", String, comment="Specifies the current time in epoch format"),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_intent_next_action_wechat_pay_redirect_to_android_app.json"]
