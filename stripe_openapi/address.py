from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

AddressJson = Table(
    "addressjson",
    metadata,
    Column(
        "city",
        String,
        comment="City, district, suburb, town, or village",
        nullable=True,
    ),
    Column(
        "country",
        String,
        comment="Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2))",
        nullable=True,
    ),
    Column(
        "line1",
        String,
        comment="Address line 1 (e.g., street, PO Box, or company name)",
        nullable=True,
    ),
    Column(
        "line2",
        String,
        comment="Address line 2 (e.g., apartment, suite, unit, or building)",
        nullable=True,
    ),
    Column("postal_code", String, comment="ZIP or postal code", nullable=True),
    Column(
        "state", String, comment="State, county, province, or region", nullable=True
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["address.json"]
