from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

PaymentFlowsAmountDetailsResourceTipJson = Table(
    "payment_flows_amount_details_resource_tipjson",
    metadata,
    Column(
        "amount",
        Integer,
        comment="Portion of the amount that corresponds to a tip",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_flows_amount_details_resource_tip.json"]
