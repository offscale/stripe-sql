from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

Recurring.Json = Table(
    "recurring.json",
    metadata,
    Column(
        "aggregate_usage",
        String,
        comment="Specifies a usage aggregation strategy for prices of `usage_type=metered`. Allowed values are `sum` for summing up all usage during a period, `last_during_period` for using the last usage record reported within a period, `last_ever` for using the last usage record ever (across period bounds) or `max` which uses the usage record with the maximum reported usage during a period. Defaults to `sum`",
        nullable=True,
    ),
    Column(
        "interval",
        String,
        comment="The frequency at which a subscription is billed. One of `day`, `week`, `month` or `year`",
    ),
    Column(
        "interval_count",
        Integer,
        comment="The number of intervals (specified in the `interval` attribute) between subscription billings. For example, `interval=month` and `interval_count=3` bills every 3 months",
    ),
    Column(
        "trial_period_days",
        Integer,
        comment="Default number of trial days when subscribing a customer to this price using [`trial_from_plan=true`](https://stripe.com/docs/api#create_subscription-trial_from_plan)",
        nullable=True,
    ),
    Column(
        "usage_type",
        String,
        comment="Configures how the quantity per period should be determined. Can be either `metered` or `licensed`. `licensed` automatically bills the `quantity` set when adding it to a subscription. `metered` aggregates the total usage based on usage records. Defaults to `licensed`",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["recurring.json"]
