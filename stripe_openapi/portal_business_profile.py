from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

PortalBusinessProfile.Json = Table(
    "portal_business_profile.json",
    metadata,
    Column(
        "headline",
        String,
        comment="The messaging shown to customers in the portal",
        nullable=True,
    ),
    Column(
        "privacy_policy_url",
        String,
        comment="A link to the business’s publicly available privacy policy",
        nullable=True,
    ),
    Column(
        "terms_of_service_url",
        String,
        comment="A link to the business’s publicly available terms of service",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["portal_business_profile.json"]
