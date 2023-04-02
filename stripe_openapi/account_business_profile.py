from sqlalchemy import Column, ForeignKey, Identity, Integer, String, Table

from stripe_openapi.address import Address

from . import metadata

AccountBusinessProfileJson = Table(
    "account_business_profilejson",
    metadata,
    Column(
        "mcc",
        String,
        comment="[The merchant category code for the account](https://stripe.com/docs/connect/setting-mcc). MCCs are used to classify businesses based on the goods or services they provide",
        nullable=True,
    ),
    Column("name", String, comment="The customer-facing business name", nullable=True),
    Column(
        "product_description",
        String,
        comment="Internal-only description of the product sold or service provided by the business. It's used by Stripe for risk and underwriting purposes",
        nullable=True,
    ),
    Column(
        "support_address",
        Address,
        ForeignKey("Address"),
        comment="A publicly available mailing address for sending support issues to",
        nullable=True,
    ),
    Column(
        "support_email",
        String,
        comment="A publicly available email address for sending support issues to",
        nullable=True,
    ),
    Column(
        "support_phone",
        String,
        comment="A publicly available phone number to call with support issues",
        nullable=True,
    ),
    Column(
        "support_url",
        String,
        comment="A publicly available website for handling support issues",
        nullable=True,
    ),
    Column(
        "url",
        String,
        comment="The business's publicly available website",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["account_business_profile.json"]
