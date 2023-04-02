from sqlalchemy import ARRAY, Boolean, Column, Identity, Integer, String, Table

from . import metadata

PortalCustomerUpdateJson = Table(
    "portal_customer_updatejson",
    metadata,
    Column(
        "allowed_updates",
        ARRAY(String),
        comment="The types of customer updates that are supported. When empty, customers are not updateable",
    ),
    Column("enabled", Boolean, comment="Whether the feature is enabled"),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["portal_customer_update.json"]
