from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

PaymentIntentNextActionWechatPayDisplayQrCodeJson = Table(
    "payment_intent_next_action_wechat_pay_display_qr_codejson",
    metadata,
    Column("data", String, comment="The data being used to generate QR code"),
    Column(
        "hosted_instructions_url",
        String,
        comment="The URL to the hosted WeChat Pay instructions page, which allows customers to view the WeChat Pay QR code",
    ),
    Column(
        "image_data_url",
        String,
        comment="The base64 image data for a pre-generated QR code",
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
__all__ = ["payment_intent_next_action_wechat_pay_display_qr_code.json"]
