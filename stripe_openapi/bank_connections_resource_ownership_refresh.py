from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

BankConnectionsResourceOwnershipRefreshJson = Table(
    "bank_connections_resource_ownership_refreshjson",
    metadata,
    Column(
        "last_attempted_at",
        Integer,
        comment="The time at which the last refresh attempt was initiated. Measured in seconds since the Unix epoch",
    ),
    Column("status", String, comment="The status of the last refresh attempt"),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["bank_connections_resource_ownership_refresh.json"]
