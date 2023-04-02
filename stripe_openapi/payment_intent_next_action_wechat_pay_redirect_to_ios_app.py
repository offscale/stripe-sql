from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

PaymentIntentNextActionWechatPayRedirectToIosAppJson = Table(
    "payment_intent_next_action_wechat_pay_redirect_to_ios_appjson",
    metadata,
    Column(
        "native_url",
        String,
        comment="An universal link that redirect to WeChat Pay app",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_intent_next_action_wechat_pay_redirect_to_ios_app.json"]
