from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

TreasuryOutboundPaymentsResourceOutboundPaymentResourceStatusTransitionsJson = Table(
    "treasury_outbound_payments_resource_outbound_payment_resource_status_transitionsjson",
    metadata,
    Column(
        "canceled_at",
        Integer,
        comment="Timestamp describing when an OutboundPayment changed status to `canceled`",
        nullable=True,
    ),
    Column(
        "failed_at",
        Integer,
        comment="Timestamp describing when an OutboundPayment changed status to `failed`",
        nullable=True,
    ),
    Column(
        "posted_at",
        Integer,
        comment="Timestamp describing when an OutboundPayment changed status to `posted`",
        nullable=True,
    ),
    Column(
        "returned_at",
        Integer,
        comment="Timestamp describing when an OutboundPayment changed status to `returned`",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = [
    "treasury_outbound_payments_resource_outbound_payment_resource_status_transitions.json"
]
