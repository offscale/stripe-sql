from sqlalchemy import ARRAY, Column, Identity, Integer, String, Table

from . import metadata

BankConnectionsResourceLinkAccountSessionFiltersJson = Table(
    "bank_connections_resource_link_account_session_filtersjson",
    metadata,
    Column(
        "countries",
        ARRAY(String),
        comment="List of countries from which to filter accounts",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["bank_connections_resource_link_account_session_filters.json"]
