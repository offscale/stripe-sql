from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

SecretServiceResourceScopeJson = Table(
    "secret_service_resource_scopejson",
    metadata,
    Column("type", String, comment="The secret scope type"),
    Column(
        "user", String, comment='The user ID, if type is set to "user"', nullable=True
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["secret_service_resource_scope.json"]
