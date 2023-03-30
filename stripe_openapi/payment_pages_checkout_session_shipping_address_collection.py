from sqlalchemy import ARRAY, Column, Identity, Integer, String, Table

from . import metadata

PaymentPagesCheckoutSessionShippingAddressCollection.Json = Table(
    "payment_pages_checkout_session_shipping_address_collection.json",
    metadata,
    Column(
        "allowed_countries",
        ARRAY(String),
        comment="An array of two-letter ISO country codes representing which countries Checkout should provide as options for\nshipping locations. Unsupported country codes: `AS, CX, CC, CU, HM, IR, KP, MH, FM, NF, MP, PW, SD, SY, UM, VI`",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_pages_checkout_session_shipping_address_collection.json"]
