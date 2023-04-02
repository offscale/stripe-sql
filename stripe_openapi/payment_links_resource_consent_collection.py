from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

PaymentLinksResourceConsentCollectionJson = Table(
    "payment_links_resource_consent_collectionjson",
    metadata,
    Column(
        "promotions",
        String,
        comment="If set to `auto`, enables the collection of customer consent for promotional communications",
        nullable=True,
    ),
    Column(
        "terms_of_service",
        String,
        comment="If set to `required`, it requires cutomers to accept the terms of service before being able to pay. If set to `none`, customers won't be shown a checkbox to accept the terms of service",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_links_resource_consent_collection.json"]
