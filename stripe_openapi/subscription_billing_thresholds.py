from sqlalchemy import Boolean, Column, Integer


class Subscription_Billing_Thresholds(Base):
    __tablename__ = "subscription_billing_thresholds"
    amount_gte = Column(
        Integer,
        comment="Monetary threshold that triggers the subscription to create an invoice",
        nullable=True,
    )
    reset_billing_cycle_anchor = Column(
        Boolean,
        comment="Indicates if the `billing_cycle_anchor` should be reset when a threshold is reached. If true, `billing_cycle_anchor` will be updated to the date/time the threshold was last reached; otherwise, the value will remain unchanged. This value may not be `true` if the subscription contains items with plans that have `aggregate_usage=last_ever`",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Subscription_Billing_Thresholds(amount_gte={amount_gte!r}, reset_billing_cycle_anchor={reset_billing_cycle_anchor!r}, id={id!r})".format(
            amount_gte=self.amount_gte,
            reset_billing_cycle_anchor=self.reset_billing_cycle_anchor,
            id=self.id,
        )


__all__ = ["subscription_billing_thresholds"]
