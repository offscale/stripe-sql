from sqlalchemy import Column, String

from . import Base


class AccountDashboardSettings(Base):
    __tablename__ = "account_dashboard_settings"
    display_name = Column(
        String,
        comment="The display name for this account. This is used on the Stripe Dashboard to differentiate between accounts",
        nullable=True,
        primary_key=True,
    )
    timezone = Column(
        String,
        comment="The timezone used in the Stripe Dashboard for this account. A list of possible time zone values is maintained at the [IANA Time Zone Database](http://www.iana.org/time-zones)",
        nullable=True,
    )

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "AccountDashboardSettings(display_name={display_name!r}, timezone={timezone!r})".format(
            display_name=self.display_name, timezone=self.timezone
        )


__all__ = ["account_dashboard_settings"]
