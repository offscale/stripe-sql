from sqlalchemy import Column, ForeignKey, String, Table

from stripe_openapi.address import Address

from . import metadata

SourceOwner.Json = Table(
    "source_owner.json",
    metadata,
    Column(
        "address",
        Address,
        ForeignKey("Address"),
        comment="Owner's address",
        nullable=True,
    ),
    Column("email", String, comment="Owner's email address", nullable=True),
    Column("name", String, comment="Owner's full name", nullable=True),
    Column(
        "phone",
        String,
        comment="Owner's phone number (including extension)",
        nullable=True,
    ),
    Column(
        "verified_address",
        Address,
        ForeignKey("Address"),
        comment="Verified owner's address. Verified values are verified or provided by the payment method directly (and if supported) at the time of authorization or settlement. They cannot be set or mutated",
        nullable=True,
    ),
    Column(
        "verified_email",
        String,
        comment="Verified owner's email address. Verified values are verified or provided by the payment method directly (and if supported) at the time of authorization or settlement. They cannot be set or mutated",
        nullable=True,
    ),
    Column(
        "verified_name",
        String,
        comment="Verified owner's full name. Verified values are verified or provided by the payment method directly (and if supported) at the time of authorization or settlement. They cannot be set or mutated",
        nullable=True,
        primary_key=True,
    ),
    Column(
        "verified_phone",
        String,
        comment="Verified owner's phone number (including extension). Verified values are verified or provided by the payment method directly (and if supported) at the time of authorization or settlement. They cannot be set or mutated",
        nullable=True,
    ),
)
__all__ = ["source_owner.json"]
