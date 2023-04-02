from sqlalchemy import Boolean, Column, Identity, Integer, Table

from . import metadata

PaymentLinksResourceTaxIdCollectionJson = Table(
    "payment_links_resource_tax_id_collectionjson",
    metadata,
    Column(
        "enabled",
        Boolean,
        comment="Indicates whether tax ID collection is enabled for the session",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_links_resource_tax_id_collection.json"]
