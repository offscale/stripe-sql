from sqlalchemy import Column, ForeignKey, Identity, Integer, Table

from . import metadata

AccountTreasurySettingsJson = Table(
    "account_treasury_settingsjson",
    metadata,
    Column(
        "tos_acceptance",
        AccountTermsOfService,
        ForeignKey("AccountTermsOfService"),
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["account_treasury_settings.json"]
