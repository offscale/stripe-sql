from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

PaymentIntentNextActionRedirectToUrl.Json = Table(
    "payment_intent_next_action_redirect_to_url.json",
    metadata,
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
__all__ = ["payment_intent_next_action_redirect_to_url.json"]
