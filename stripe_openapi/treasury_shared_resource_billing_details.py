from sqlalchemy import Column, ForeignKey, Identity, Integer, String, Table

from stripe_openapi.address import Address

from . import metadata

TreasurySharedResourceBillingDetails.Json = Table(
    "treasury_shared_resource_billing_details.json",
    metadata,
    Column("address", Address, ForeignKey("Address")),
    Column("email", String, comment="Email address", nullable=True),
    Column("name", String, comment="Full name", nullable=True),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["treasury_shared_resource_billing_details.json"]
