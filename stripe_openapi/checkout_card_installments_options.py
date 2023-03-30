from sqlalchemy import Boolean, Column, Identity, Integer, Table

from . import metadata

CheckoutCardInstallmentsOptions.Json = Table(
    "checkout_card_installments_options.json",
    metadata,
    Column(
        "enabled",
        Boolean,
        comment="Indicates if installments are enabled",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["checkout_card_installments_options.json"]
