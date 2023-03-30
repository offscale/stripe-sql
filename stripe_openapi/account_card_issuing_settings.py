from sqlalchemy import Column, ForeignKey, Identity, Integer, Table

from . import metadata

AccountCardIssuingSettings.Json = Table(
    "account_card_issuing_settings.json",
    metadata,
    Column(
        "tos_acceptance",
        CardIssuingAccountTermsOfService,
        ForeignKey("CardIssuingAccountTermsOfService"),
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["account_card_issuing_settings.json"]
