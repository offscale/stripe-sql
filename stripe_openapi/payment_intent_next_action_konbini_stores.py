from sqlalchemy import Column, ForeignKey, Identity, Integer, Table

from . import metadata

PaymentIntentNextActionKonbiniStores.Json = Table(
    "payment_intent_next_action_konbini_stores.json",
    metadata,
    Column(
        "familymart",
        PaymentIntentNextActionKonbiniFamilymart,
        ForeignKey("PaymentIntentNextActionKonbiniFamilymart"),
        comment="FamilyMart instruction details",
        nullable=True,
    ),
    Column(
        "lawson",
        PaymentIntentNextActionKonbiniLawson,
        ForeignKey("PaymentIntentNextActionKonbiniLawson"),
        comment="Lawson instruction details",
        nullable=True,
    ),
    Column(
        "ministop",
        PaymentIntentNextActionKonbiniMinistop,
        ForeignKey("PaymentIntentNextActionKonbiniMinistop"),
        comment="Ministop instruction details",
        nullable=True,
    ),
    Column(
        "seicomart",
        PaymentIntentNextActionKonbiniSeicomart,
        ForeignKey("PaymentIntentNextActionKonbiniSeicomart"),
        comment="Seicomart instruction details",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_intent_next_action_konbini_stores.json"]
