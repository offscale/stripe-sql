from sqlalchemy import Boolean, Column, Identity, Integer, Table

from . import metadata

PaymentLinksResourcePhoneNumberCollection.Json = Table(
    "payment_links_resource_phone_number_collection.json",
    metadata,
    Column(
        "enabled",
        Boolean,
        comment="If `true`, a phone number will be collected during checkout",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_links_resource_phone_number_collection.json"]
