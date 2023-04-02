from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

PaymentMethodDetailsKonbiniStoreJson = Table(
    "payment_method_details_konbini_storejson",
    metadata,
    Column(
        "chain",
        String,
        comment="The name of the convenience store chain where the payment was completed",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_method_details_konbini_store.json"]
