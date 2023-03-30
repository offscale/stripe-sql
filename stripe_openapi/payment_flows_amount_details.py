from sqlalchemy import Column, ForeignKey, Identity, Integer, Table

from . import metadata

PaymentFlowsAmountDetails.Json = Table(
    "payment_flows_amount_details.json",
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
