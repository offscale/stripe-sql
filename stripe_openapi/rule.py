from sqlalchemy import Column, String, Table

from . import metadata

Rule.Json = Table(
    "rule.json",
    metadata,
    Column("action", String, comment="The action taken on the payment"),
    Column("id", String, comment="Unique identifier for the object", primary_key=True),
    Column(
        "predicate", String, comment="The predicate to evaluate the payment against"
    ),
)
__all__ = ["rule.json"]
