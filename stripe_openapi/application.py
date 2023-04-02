from sqlalchemy import Column, String, Table

from . import metadata

ApplicationJson = Table(
    "applicationjson",
    metadata,
    Column("id", String, comment="Unique identifier for the object", primary_key=True),
    Column("name", String, comment="The name of the application", nullable=True),
    Column(
        "object",
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    ),
)
__all__ = ["application.json"]
