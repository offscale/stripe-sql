from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

PaymentIntentNextActionPaynowDisplayQrCode.Json = Table(
    "payment_intent_next_action_paynow_display_qr_code.json",
    metadata,
    Column(
        "data",
        String,
        comment="The raw data string used to generate QR code, it should be used together with QR code library",
    ),
    Column(
        "hosted_instructions_url",
        String,
        comment="The URL to the hosted PayNow instructions page, which allows customers to view the PayNow QR code",
        nullable=True,
    ),
    Column(
        "image_url_png",
        String,
        comment="The image_url_png string used to render QR code",
    ),
    Column(
        "image_url_svg",
        String,
        comment="The image_url_svg string used to render QR code",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_intent_next_action_paynow_display_qr_code.json"]
