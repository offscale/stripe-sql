from sqlalchemy import Boolean, Column, String, Table

from . import metadata

DeletedApplePayDomain.Json = Table(
    "deleted_apple_pay_domain.json",
    metadata,
    Column("deleted", Boolean, comment="Always true for a deleted object"),
    Column("id", String, comment="Unique identifier for the object", primary_key=True),
    Column(
        "object",
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    ),
)
__all__ = ["deleted_apple_pay_domain.json"]
