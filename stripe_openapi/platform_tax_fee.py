from sqlalchemy import Column, String, Table

from . import metadata

PlatformTaxFeeJson = Table(
    "platform_tax_feejson",
    metadata,
    Column(
        "account", String, comment="The Connected account that incurred this charge"
    ),
    Column("id", String, comment="Unique identifier for the object", primary_key=True),
    Column(
        "object",
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    ),
    Column(
        "source_transaction",
        String,
        comment="The payment object that caused this tax to be inflicted",
    ),
    Column("type", String, comment="The type of tax (VAT)"),
)
__all__ = ["platform_tax_fee.json"]
