from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

PaymentIntentNextActionPixDisplayQrCodeJson = Table(
    "payment_intent_next_action_pix_display_qr_codejson",
    metadata,
    Column(
        "data",
        String,
        comment="The raw data string used to generate QR code, it should be used together with QR code library",
        nullable=True,
    ),
    Column(
        "expires_at",
        Integer,
        comment="The date (unix timestamp) when the PIX expires",
        nullable=True,
    ),
    Column(
        "hosted_instructions_url",
        String,
        comment="The URL to the hosted pix instructions page, which allows customers to view the pix QR code",
        nullable=True,
    ),
    Column(
        "image_url_png",
        String,
        comment="The image_url_png string used to render png QR code",
        nullable=True,
    ),
    Column(
        "image_url_svg",
        String,
        comment="The image_url_svg string used to render svg QR code",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_intent_next_action_pix_display_qr_code.json"]
