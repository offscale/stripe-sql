from sqlalchemy import Column, ForeignKey, Identity, Integer, Table

from . import metadata

AccountSettings.Json = Table(
    "account_settings.json",
    metadata,
    Column(
        "bacs_debit_payments",
        AccountBacsDebitPaymentsSettings,
        ForeignKey("AccountBacsDebitPaymentsSettings"),
        nullable=True,
    ),
    Column("branding", AccountBrandingSettings, ForeignKey("AccountBrandingSettings")),
    Column(
        "card_issuing",
        AccountCardIssuingSettings,
        ForeignKey("AccountCardIssuingSettings"),
        nullable=True,
    ),
    Column(
        "card_payments",
        AccountCardPaymentsSettings,
        ForeignKey("AccountCardPaymentsSettings"),
    ),
    Column(
        "dashboard", AccountDashboardSettings, ForeignKey("AccountDashboardSettings")
    ),
    Column("payments", AccountPaymentsSettings, ForeignKey("AccountPaymentsSettings")),
    Column(
        "payouts",
        AccountPayoutSettings,
        ForeignKey("AccountPayoutSettings"),
        nullable=True,
    ),
    Column(
        "sepa_debit_payments",
        AccountSepaDebitPaymentsSettings,
        ForeignKey("AccountSepaDebitPaymentsSettings"),
        nullable=True,
    ),
    Column(
        "treasury",
        AccountTreasurySettings,
        ForeignKey("AccountTreasurySettings"),
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["account_settings.json"]
