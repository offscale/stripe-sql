from sqlalchemy import Column, String, Table

from . import metadata

IssuingAuthorizationMerchantData.Json = Table(
    "issuing_authorization_merchant_data.json",
    metadata,
    Column(
        "category",
        String,
        comment="A categorization of the seller's type of business. See our [merchant categories guide](https://stripe.com/docs/issuing/merchant-categories) for a list of possible values",
    ),
    Column(
        "category_code",
        String,
        comment="The merchant category code for the seller’s business",
    ),
    Column("city", String, comment="City where the seller is located", nullable=True),
    Column(
        "country", String, comment="Country where the seller is located", nullable=True
    ),
    Column("name", String, comment="Name of the seller", nullable=True),
    Column(
        "network_id",
        String,
        comment="Identifier assigned to the seller by the card network. Different card networks may assign different network_id fields to the same merchant",
        primary_key=True,
    ),
    Column(
        "postal_code",
        String,
        comment="Postal code where the seller is located",
        nullable=True,
    ),
    Column("state", String, comment="State where the seller is located", nullable=True),
)
__all__ = ["issuing_authorization_merchant_data.json"]
