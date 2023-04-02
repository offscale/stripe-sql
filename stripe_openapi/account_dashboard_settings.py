from sqlalchemy import Column, String, Table

from . import metadata

AccountDashboardSettingsJson = Table(
    "account_dashboard_settingsjson",
    metadata,
    Column(
        "display_name",
        String,
        comment="The display name for this account. This is used on the Stripe Dashboard to differentiate between accounts",
        nullable=True,
        primary_key=True,
    ),
    Column(
        "timezone",
        String,
        comment="The timezone used in the Stripe Dashboard for this account. A list of possible time zone values is maintained at the [IANA Time Zone Database](http://www.iana.org/time-zones)",
        nullable=True,
    ),
)
__all__ = ["account_dashboard_settings.json"]
