from sqlalchemy import Boolean, Column, Integer, String


class Portal_Subscription_Cancel(Base):
    __tablename__ = "portal_subscription_cancel"
    cancellation_reason = Column(
        portal_subscription_cancellation_reason,
        ForeignKey("portal_subscription_cancellation_reason"),
    )
    enabled = Column(Boolean, comment="Whether the feature is enabled")
    mode = Column(
        String,
        comment="Whether to cancel subscriptions immediately or at the end of the billing period",
    )
    proration_behavior = Column(
        String,
        comment="Whether to create prorations when canceling subscriptions. Possible values are `none` and `create_prorations`",
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Portal_Subscription_Cancel(cancellation_reason={cancellation_reason!r}, enabled={enabled!r}, mode={mode!r}, proration_behavior={proration_behavior!r}, id={id!r})".format(
            cancellation_reason=self.cancellation_reason,
            enabled=self.enabled,
            mode=self.mode,
            proration_behavior=self.proration_behavior,
            id=self.id,
        )


__all__ = ["portal_subscription_cancel"]
