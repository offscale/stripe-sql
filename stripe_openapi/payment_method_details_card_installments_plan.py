from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

PaymentMethodDetailsCardInstallmentsPlanJson = Table(
    "payment_method_details_card_installments_planjson",
    metadata,
    Column(
        "count",
        Integer,
        comment="For `fixed_count` installment plans, this is the number of installment payments your customer will make to their credit card",
        nullable=True,
    ),
    Column(
        "interval",
        String,
        comment="For `fixed_count` installment plans, this is the interval between installment payments your customer will make to their credit card.\nOne of `month`",
        nullable=True,
    ),
    Column("type", String, comment="Type of installment plan, one of `fixed_count`"),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_method_details_card_installments_plan.json"]
