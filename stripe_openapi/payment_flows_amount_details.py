from sqlalchemy import Column, ForeignKey, Identity, Integer, Table

from . import metadata

PaymentFlowsAmountDetailsJson = Table(
    "payment_flows_amount_detailsjson",
    metadata,
    Column(
        "tip",
        PaymentFlowsAmountDetailsResourceTip,
        ForeignKey("PaymentFlowsAmountDetailsResourceTip"),
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_flows_amount_details.json"]
