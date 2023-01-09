from sqlalchemy import Boolean, Column, Identity, Integer

from . import Base


class PortalSubscriptionPause(Base):
    __tablename__ = "portal_subscription_pause"
    enabled = Column(Boolean, comment="Whether the feature is enabled")
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "PortalSubscriptionPause(enabled={enabled!r}, id={id!r})".format(
            enabled=self.enabled, id=self.id
        )


__all__ = ["portal_subscription_pause"]
