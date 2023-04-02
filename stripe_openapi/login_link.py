from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

LoginLinkJson = Table(
    "login_linkjson",
    metadata,
    Column(
        "created",
        Integer,
        comment="Time at which the object was created. Measured in seconds since the Unix epoch",
    ),
    Column(
        "object",
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    ),
    Column("url", String, comment="The URL for the login link"),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["login_link.json"]
