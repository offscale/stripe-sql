from sqlalchemy import Boolean, Column, Identity, Integer, list

from . import Base


class SubscriptionsResourcePendingUpdate(Base):
    """
    Pending Updates store the changes pending from a previous update that will be applied

    to the Subscription upon successful payment.

    """

    __tablename__ = "subscriptions_resource_pending_update"
    billing_cycle_anchor = Column(
        Integer,
        comment="If the update is applied, determines the date of the first full invoice, and, for plans with `month` or `year` intervals, the day of the month for subsequent invoices. The timestamp is in UTC format",
        nullable=True,
    )
    expires_at = Column(
        Integer,
        comment="The point after which the changes reflected by this update will be discarded and no longer applied",
    )
    subscription_items = Column(
        list,
        comment="List of subscription items, each with an attached plan, that will be set if the update is applied",
        nullable=True,
    )
    trial_end = Column(
        Integer,
        comment="Unix timestamp representing the end of the trial period the customer will get before being charged for the first time, if the update is applied",
        nullable=True,
    )
    trial_from_plan = Column(
        Boolean,
        comment="Indicates if a plan's `trial_period_days` should be applied to the subscription. Setting `trial_end` per subscription is preferred, and this defaults to `false`. Setting this flag to `true` together with `trial_end` is not allowed. See [Using trial periods on subscriptions](https://stripe.com/docs/billing/subscriptions/trials) to learn more",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "SubscriptionsResourcePendingUpdate(billing_cycle_anchor={billing_cycle_anchor!r}, expires_at={expires_at!r}, subscription_items={subscription_items!r}, trial_end={trial_end!r}, trial_from_plan={trial_from_plan!r}, id={id!r})".format(
            billing_cycle_anchor=self.billing_cycle_anchor,
            expires_at=self.expires_at,
            subscription_items=self.subscription_items,
            trial_end=self.trial_end,
            trial_from_plan=self.trial_from_plan,
            id=self.id,
        )


__all__ = ["subscriptions_resource_pending_update"]
