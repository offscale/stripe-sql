from sqlalchemy import Column, ForeignKey, Identity, Integer, Table

from . import metadata

RefundNextActionDisplayDetails.Json = Table(
    "refund_next_action_display_details.json",
    metadata,
    Column("email_sent", EmailSent, ForeignKey("EmailSent")),
    Column("expires_at", Integer, comment="The expiry timestamp"),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["refund_next_action_display_details.json"]
