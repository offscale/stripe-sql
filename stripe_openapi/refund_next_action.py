from sqlalchemy import Column, ForeignKey, Identity, Integer, String, Table

from . import metadata

RefundNextAction.Json = Table(
    "refund_next_action.json",
    metadata,
    Column(
        "display_details",
        RefundNextActionDisplayDetails,
        ForeignKey("RefundNextActionDisplayDetails"),
        comment="Contains the refund details",
        nullable=True,
    ),
    Column("type", String, comment="Type of the next action to perform"),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["refund_next_action.json"]
