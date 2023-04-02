from sqlalchemy import Boolean, Column, Identity, Integer, Table

from . import metadata

SubscriptionSchedulesResourceDefaultSettingsAutomaticTaxJson = Table(
    "subscription_schedules_resource_default_settings_automatic_taxjson",
    metadata,
    Column(
        "enabled",
        Boolean,
        comment="Whether Stripe automatically computes tax on invoices created during this phase",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["subscription_schedules_resource_default_settings_automatic_tax.json"]
