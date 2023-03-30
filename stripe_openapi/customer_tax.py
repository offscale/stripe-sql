from sqlalchemy import Column, ForeignKey, Identity, Integer, String, Table

from . import metadata

CustomerTax.Json = Table(
    "customer_tax.json",
    metadata,
    Column(
        "automatic_tax",
        String,
        comment="Surfaces if automatic tax computation is possible given the current customer location information",
    ),
    Column(
        "ip_address",
        String,
        comment="A recent IP address of the customer used for tax reporting and tax location inference",
        nullable=True,
    ),
    Column(
        "location",
        CustomerTaxLocation,
        ForeignKey("CustomerTaxLocation"),
        comment="The customer's location as identified by Stripe Tax",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["customer_tax.json"]
