from sqlalchemy import Boolean, Column, ForeignKey, Identity, Integer, String, Table

from stripe_openapi.address import Address

from . import metadata

IssuingCardShippingJson = Table(
    "issuing_card_shippingjson",
    metadata,
    Column("address", Address, ForeignKey("Address")),
    Column(
        "carrier",
        String,
        comment="The delivery company that shipped a card",
        nullable=True,
    ),
    Column(
        "customs",
        IssuingCardShippingCustoms,
        ForeignKey("IssuingCardShippingCustoms"),
        comment="Additional information that may be required for clearing customs",
        nullable=True,
    ),
    Column(
        "eta",
        Integer,
        comment="A unix timestamp representing a best estimate of when the card will be delivered",
        nullable=True,
    ),
    Column("name", String, comment="Recipient name"),
    Column(
        "phone_number",
        String,
        comment="The phone number of the receiver of the bulk shipment. This phone number will be provided to the shipping company, who might use it to contact the receiver in case of delivery issues",
        nullable=True,
    ),
    Column(
        "require_signature",
        Boolean,
        comment="Whether a signature is required for card delivery. This feature is only supported for US users. Standard shipping service does not support signature on delivery. The default value for standard shipping service is false and for express and priority services is true",
        nullable=True,
    ),
    Column(
        "service", String, comment="Shipment service, such as `standard` or `express`"
    ),
    Column("status", String, comment="The delivery status of the card", nullable=True),
    Column(
        "tracking_number",
        String,
        comment="A tracking number for a card shipment",
        nullable=True,
    ),
    Column(
        "tracking_url",
        String,
        comment="A link to the shipping carrier's site where you can view detailed information about a card shipment",
        nullable=True,
    ),
    Column("type", String, comment="Packaging options"),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["issuing_card_shipping.json"]
