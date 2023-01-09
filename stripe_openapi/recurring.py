from sqlalchemy import Column, Identity, Integer, String

from . import Base


class Recurring(Base):
    __tablename__ = "recurring"
    aggregate_usage = Column(
        String,
        comment="Specifies a usage aggregation strategy for prices of `usage_type=metered`. Allowed values are `sum` for summing up all usage during a period, `last_during_period` for using the last usage record reported within a period, `last_ever` for using the last usage record ever (across period bounds) or `max` which uses the usage record with the maximum reported usage during a period. Defaults to `sum`",
        nullable=True,
    )
    interval = Column(
        String,
        comment="The frequency at which a subscription is billed. One of `day`, `week`, `month` or `year`",
    )
    interval_count = Column(
        Integer,
        comment="The number of intervals (specified in the `interval` attribute) between subscription billings. For example, `interval=month` and `interval_count=3` bills every 3 months",
    )
    trial_period_days = Column(
        Integer,
        comment="Default number of trial days when subscribing a customer to this price using [`trial_from_plan=true`](https://stripe.com/docs/api#create_subscription-trial_from_plan)",
        nullable=True,
    )
    usage_type = Column(
        String,
        comment="Configures how the quantity per period should be determined. Can be either `metered` or `licensed`. `licensed` automatically bills the `quantity` set when adding it to a subscription. `metered` aggregates the total usage based on usage records. Defaults to `licensed`",
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Recurring(aggregate_usage={aggregate_usage!r}, interval={interval!r}, interval_count={interval_count!r}, trial_period_days={trial_period_days!r}, usage_type={usage_type!r}, id={id!r})".format(
            aggregate_usage=self.aggregate_usage,
            interval=self.interval,
            interval_count=self.interval_count,
            trial_period_days=self.trial_period_days,
            usage_type=self.usage_type,
            id=self.id,
        )


__all__ = ["recurring"]
