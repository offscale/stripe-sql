from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

LegalEntityJapanAddress.Json = Table(
    "legal_entity_japan_address.json",
    metadata,
    Column("city", String, comment="City/Ward", nullable=True),
    Column(
        "country",
        String,
        comment="Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2))",
        nullable=True,
    ),
    Column("line1", String, comment="Block/Building number", nullable=True),
    Column("line2", String, comment="Building details", nullable=True),
    Column("postal_code", String, comment="ZIP or postal code", nullable=True),
    Column("state", String, comment="Prefecture", nullable=True),
    Column("town", String, comment="Town/cho-me", nullable=True),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["legal_entity_japan_address.json"]
