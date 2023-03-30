from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

PaymentIntentNextActionAlipayHandleRedirect.Json = Table(
    "payment_intent_next_action_alipay_handle_redirect.json",
    metadata,
    Column(
        "native_data",
        String,
        comment="The native data to be used with Alipay SDK you must redirect your customer to in order to authenticate the payment in an Android App",
        nullable=True,
    ),
    Column(
        "native_url",
        String,
        comment="The native URL you must redirect your customer to in order to authenticate the payment in an iOS App",
        nullable=True,
    ),
    Column(
        "return_url",
        String,
        comment="If the customer does not exit their browser while authenticating, they will be redirected to this specified URL after completion",
        nullable=True,
    ),
    Column(
        "url",
        String,
        comment="The URL you must redirect your customer to in order to authenticate the payment",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_intent_next_action_alipay_handle_redirect.json"]
