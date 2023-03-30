from sqlalchemy import Column, ForeignKey, Identity, Integer, Table

from . import metadata

PaymentMethodDetailsCardInstallments.Json = Table(
    "payment_method_details_card_installments.json",
    metadata,
    Column(
        "plan",
        PaymentMethodDetailsCardInstallmentsPlan,
        ForeignKey("PaymentMethodDetailsCardInstallmentsPlan"),
        comment="Installment plan selected for the payment",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_method_details_card_installments.json"]
