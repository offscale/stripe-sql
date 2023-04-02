from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

PaymentMethodDetailsMultibancoJson = Table(
    "payment_method_details_multibancojson",
    metadata,
    Column(
        "entity",
        String,
        comment="Entity number associated with this Multibanco payment",
        nullable=True,
    ),
    Column(
        "reference",
        String,
        comment="Reference number associated with this Multibanco payment",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_method_details_multibanco.json"]
