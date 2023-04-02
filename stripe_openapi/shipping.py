from sqlalchemy import Column, ForeignKey, Identity, Integer, String, Table

from stripe_openapi.address import Address

from . import metadata

ShippingJson = Table(
    "shippingjson",
    metadata,
    Column("address", Address, ForeignKey("Address"), nullable=True),
    Column(
        "carrier",
        String,
        comment="The delivery service that shipped a physical product, such as Fedex, UPS, USPS, etc",
        nullable=True,
    ),
    Column("name", String, comment="Recipient name", nullable=True),
    Column(
        "phone", String, comment="Recipient phone (including extension)", nullable=True
    ),
    Column(
        "tracking_number",
        String,
        comment="The tracking number for a physical product, obtained from the delivery service. If multiple tracking numbers were generated for this purchase, please separate them with commas",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["shipping.json"]
