from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

QuotesResourceStatusTransitions.Json = Table(
    "quotes_resource_status_transitions.json",
    metadata,
    Column(
        "accepted_at",
        Integer,
        comment="The time that the quote was accepted. Measured in seconds since Unix epoch",
        nullable=True,
    ),
    Column(
        "canceled_at",
        Integer,
        comment="The time that the quote was canceled. Measured in seconds since Unix epoch",
        nullable=True,
    ),
    Column(
        "finalized_at",
        Integer,
        comment="The time that the quote was finalized. Measured in seconds since Unix epoch",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["quotes_resource_status_transitions.json"]
