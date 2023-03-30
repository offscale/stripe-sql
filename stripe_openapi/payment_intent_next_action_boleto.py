from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

PaymentIntentNextActionBoleto.Json = Table(
    "payment_intent_next_action_boleto.json",
    metadata,
    Column(
        "expires_at",
        Integer,
        comment="The timestamp after which the boleto expires",
        nullable=True,
    ),
    Column(
        "hosted_voucher_url",
        String,
        comment="The URL to the hosted boleto voucher page, which allows customers to view the boleto voucher",
        nullable=True,
    ),
    Column("number", String, comment="The boleto number", nullable=True),
    Column(
        "pdf",
        String,
        comment="The URL to the downloadable boleto voucher PDF",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_intent_next_action_boleto.json"]
