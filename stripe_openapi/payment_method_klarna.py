from sqlalchemy import Column, ForeignKey, Identity, Integer, Table

from . import metadata

PaymentMethodKlarna.Json = Table(
    "payment_method_klarna.json",
    metadata,
    Column(
        "dob",
        PaymentFlowsPrivatePaymentMethodsKlarnaDob,
        ForeignKey("PaymentFlowsPrivatePaymentMethodsKlarnaDob"),
        comment="The customer's date of birth, if provided",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_method_klarna.json"]
