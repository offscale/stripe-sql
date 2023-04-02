from sqlalchemy import Boolean, Column, ForeignKey, Identity, Integer, Table, list

from . import metadata

PaymentMethodOptionsCardInstallmentsJson = Table(
    "payment_method_options_card_installmentsjson",
    metadata,
    Column(
        "available_plans",
        list,
        comment="Installment plans that may be selected for this PaymentIntent",
        nullable=True,
    ),
    Column(
        "enabled",
        Boolean,
        comment="Whether Installments are enabled for this PaymentIntent",
    ),
    Column(
        "plan",
        PaymentMethodDetailsCardInstallmentsPlan,
        ForeignKey("PaymentMethodDetailsCardInstallmentsPlan"),
        comment="Installment plan selected for this PaymentIntent",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_method_options_card_installments.json"]
