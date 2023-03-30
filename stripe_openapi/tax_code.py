from sqlalchemy import Column, String, Table

from . import metadata

TaxCode.Json = Table(
    "tax_code.json",
    metadata,
    Column(
        "description",
        String,
        comment="A detailed description of which types of products the tax code represents",
    ),
    Column("id", String, comment="Unique identifier for the object", primary_key=True),
    Column("name", String, comment="A short name for the tax code"),
    Column(
        "object",
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    ),
)
__all__ = ["tax_code.json"]
