from sqlalchemy import Boolean, Column, ForeignKey, Identity, Integer, Table

from . import metadata

PaymentFlowsInstallmentOptionsJson = Table(
    "payment_flows_installment_optionsjson",
    metadata,
    Column("enabled", Boolean),
    Column(
        "plan",
        PaymentMethodDetailsCardInstallmentsPlan,
        ForeignKey("PaymentMethodDetailsCardInstallmentsPlan"),
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_flows_installment_options.json"]
