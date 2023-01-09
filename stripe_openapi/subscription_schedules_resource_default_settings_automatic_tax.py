from sqlalchemy import Boolean, Column, Identity, Integer

from . import Base


class SubscriptionSchedulesResourceDefaultSettingsAutomaticTax(Base):
    __tablename__ = "subscription_schedules_resource_default_settings_automatic_tax"
    enabled = Column(
        Boolean,
        comment="Whether Stripe automatically computes tax on invoices created during this phase",
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "SubscriptionSchedulesResourceDefaultSettingsAutomaticTax(enabled={enabled!r}, id={id!r})".format(
            enabled=self.enabled, id=self.id
        )


__all__ = ["subscription_schedules_resource_default_settings_automatic_tax"]
