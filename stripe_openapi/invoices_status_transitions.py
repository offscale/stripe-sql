from sqlalchemy import Column, Integer, Table

from . import metadata

InvoicesStatusTransitionsJson = Table(
    "invoices_status_transitionsjson",
    metadata,
    Column(
        "finalized_at",
        Integer,
        comment="The time that the invoice draft was finalized",
        nullable=True,
    ),
    Column(
        "marked_uncollectible_at",
        Integer,
        comment="The time that the invoice was marked uncollectible",
        nullable=True,
    ),
    Column(
        "paid_at",
        Integer,
        comment="The time that the invoice was paid",
        nullable=True,
        primary_key=True,
    ),
    Column(
        "voided_at",
        Integer,
        comment="The time that the invoice was voided",
        nullable=True,
    ),
)
__all__ = ["invoices_status_transitions.json"]
