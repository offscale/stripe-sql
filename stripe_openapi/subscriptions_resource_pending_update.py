from sqlalchemy import Boolean, Column, Identity, Integer, Table, list

from . import metadata

SubscriptionsResourcePendingUpdateJson = Table(
    "subscriptions_resource_pending_updatejson",
    metadata,
    Column(
        "billing_cycle_anchor",
        Integer,
        comment="If the update is applied, determines the date of the first full invoice, and, for plans with `month` or `year` intervals, the day of the month for subsequent invoices. The timestamp is in UTC format",
        nullable=True,
    ),
    Column(
        "expires_at",
        Integer,
        comment="The point after which the changes reflected by this update will be discarded and no longer applied",
    ),
    Column(
        "subscription_items",
        list,
        comment="List of subscription items, each with an attached plan, that will be set if the update is applied",
        nullable=True,
    ),
    Column(
        "trial_end",
        Integer,
        comment="Unix timestamp representing the end of the trial period the customer will get before being charged for the first time, if the update is applied",
        nullable=True,
    ),
    Column(
        "trial_from_plan",
        Boolean,
        comment="Indicates if a plan's `trial_period_days` should be applied to the subscription. Setting `trial_end` per subscription is preferred, and this defaults to `false`. Setting this flag to `true` together with `trial_end` is not allowed. See [Using trial periods on subscriptions](https://stripe.com/docs/billing/subscriptions/trials) to learn more",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["subscriptions_resource_pending_update.json"]
