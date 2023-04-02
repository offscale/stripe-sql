from sqlalchemy import Column, ForeignKey, Identity, Integer, Table

from stripe_openapi.charge import Charge

from . import metadata

SepaDebitGeneratedFromJson = Table(
    "sepa_debit_generated_fromjson",
    metadata,
    Column(
        "charge",
        Charge,
        ForeignKey("Charge"),
        comment="The ID of the Charge that generated this PaymentMethod, if any",
        nullable=True,
    ),
    Column(
        "setup_attempt",
        SetupAttempt,
        ForeignKey("SetupAttempt"),
        comment="The ID of the SetupAttempt that generated this PaymentMethod, if any",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["sepa_debit_generated_from.json"]
