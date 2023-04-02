from sqlalchemy import Column, ForeignKey, Identity, Integer, String, Table

from stripe_openapi.address import Address

from . import metadata

BillingDetailsJson = Table(
    "billing_detailsjson",
    metadata,
    Column(
        "address",
        Address,
        ForeignKey("Address"),
        comment="Billing address",
        nullable=True,
    ),
    Column("email", String, comment="Email address", nullable=True),
    Column("name", String, comment="Full name", nullable=True),
    Column(
        "phone",
        String,
        comment="Billing phone number (including extension)",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["billing_details.json"]
