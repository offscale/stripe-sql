from sqlalchemy import Column, ForeignKey, Identity, Integer, Table

from . import metadata

PaymentMethodDetailsKonbini.Json = Table(
    "payment_method_details_konbini.json",
    metadata,
    Column(
        "store",
        PaymentMethodDetailsKonbiniStore,
        ForeignKey("PaymentMethodDetailsKonbiniStore"),
        comment="If the payment succeeded, this contains the details of the convenience store where the payment was completed",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_method_details_konbini.json"]
