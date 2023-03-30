from sqlalchemy import Boolean, Column, Identity, Integer, Table

from . import metadata

PaymentFlowsAutomaticPaymentMethodsPaymentIntent.Json = Table(
    "payment_flows_automatic_payment_methods_payment_intent.json",
    metadata,
    Column(
        "enabled",
        Boolean,
        comment="Automatically calculates compatible payment methods",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_flows_automatic_payment_methods_payment_intent.json"]
