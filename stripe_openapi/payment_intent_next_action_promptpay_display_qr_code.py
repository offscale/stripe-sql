from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

PaymentIntentNextActionPromptpayDisplayQrCode.Json = Table(
    "payment_intent_next_action_promptpay_display_qr_code.json",
    metadata,
    Column(
        "data",
        String,
        comment="The raw data string used to generate QR code, it should be used together with QR code library",
    ),
    Column(
        "hosted_instructions_url",
        String,
        comment="The URL to the hosted PromptPay instructions page, which allows customers to view the PromptPay QR code",
    ),
    Column(
        "image_url_png",
        String,
        comment="The PNG path used to render the QR code, can be used as the source in an HTML img tag",
    ),
    Column(
        "image_url_svg",
        String,
        comment="The SVG path used to render the QR code, can be used as the source in an HTML img tag",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_intent_next_action_promptpay_display_qr_code.json"]
