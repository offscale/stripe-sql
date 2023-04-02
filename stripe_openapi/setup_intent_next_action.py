from sqlalchemy import JSON, Column, ForeignKey, Identity, Integer, String, Table

from . import metadata

SetupIntentNextActionJson = Table(
    "setup_intent_next_actionjson",
    metadata,
    Column(
        "cashapp_handle_redirect_or_display_qr_code",
        PaymentIntentNextActionCashappHandleRedirectOrDisplayQrCode,
        ForeignKey("PaymentIntentNextActionCashappHandleRedirectOrDisplayQrCode"),
        nullable=True,
    ),
    Column(
        "redirect_to_url",
        SetupIntentNextActionRedirectToUrl,
        ForeignKey("SetupIntentNextActionRedirectToUrl"),
        nullable=True,
    ),
    Column(
        "type",
        String,
        comment="Type of the next action to perform, one of `redirect_to_url`, `use_stripe_sdk`, `alipay_handle_redirect`, `oxxo_display_details`, or `verify_with_microdeposits`",
    ),
    Column(
        "use_stripe_sdk",
        JSON,
        comment="When confirming a SetupIntent with Stripe.js, Stripe.js depends on the contents of this dictionary to invoke authentication flows. The shape of the contents is subject to change and is only intended to be used by Stripe.js",
        nullable=True,
    ),
    Column(
        "verify_with_microdeposits",
        SetupIntentNextActionVerifyWithMicrodeposits,
        ForeignKey("SetupIntentNextActionVerifyWithMicrodeposits"),
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["setup_intent_next_action.json"]
