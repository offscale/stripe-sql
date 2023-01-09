from sqlalchemy import ARRAY, Boolean, Column, Identity, Integer, String

from . import Base


class PortalSubscriptionCancellationReason(Base):
    __tablename__ = "portal_subscription_cancellation_reason"
    enabled = Column(Boolean, comment="Whether the feature is enabled")
    options = Column(
        ARRAY(String),
        comment="Which cancellation reasons will be given as options to the customer",
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "PortalSubscriptionCancellationReason(enabled={enabled!r}, options={options!r}, id={id!r})".format(
            enabled=self.enabled, options=self.options, id=self.id
        )


__all__ = ["portal_subscription_cancellation_reason"]
