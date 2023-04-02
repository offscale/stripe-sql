from sqlalchemy import JSON, Boolean, Column, ForeignKey, Integer, String, Table, list

from stripe_openapi.product import Product

from . import metadata

PlanJson = Table(
    "planjson",
    metadata,
    Column("active", Boolean, comment="Whether the plan can be used for new purchases"),
    Column(
        "aggregate_usage",
        String,
        comment="Specifies a usage aggregation strategy for plans of `usage_type=metered`. Allowed values are `sum` for summing up all usage during a period, `last_during_period` for using the last usage record reported within a period, `last_ever` for using the last usage record ever (across period bounds) or `max` which uses the usage record with the maximum reported usage during a period. Defaults to `sum`",
        nullable=True,
    ),
    Column(
        "amount",
        Integer,
        comment="The unit amount in %s to be charged, represented as a whole integer if possible. Only set if `billing_scheme=per_unit`",
        nullable=True,
    ),
    Column(
        "amount_decimal",
        String,
        comment="The unit amount in %s to be charged, represented as a decimal string with at most 12 decimal places. Only set if `billing_scheme=per_unit`",
        nullable=True,
    ),
    Column(
        "billing_scheme",
        String,
        comment="Describes how to compute the price per period. Either `per_unit` or `tiered`. `per_unit` indicates that the fixed amount (specified in `amount`) will be charged per unit in `quantity` (for plans with `usage_type=licensed`), or per unit of total usage (for plans with `usage_type=metered`). `tiered` indicates that the unit pricing will be computed using a tiering strategy as defined using the `tiers` and `tiers_mode` attributes",
    ),
    Column(
        "created",
        Integer,
        comment="Time at which the object was created. Measured in seconds since the Unix epoch",
    ),
    Column(
        "currency",
        String,
        comment="Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)",
    ),
    Column("id", String, comment="Unique identifier for the object", primary_key=True),
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
        "livemode",
        Boolean,
        comment="Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode",
    ),
    Column(
        "metadata",
        JSON,
        comment="Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format",
        nullable=True,
    ),
    Column(
        "nickname",
        String,
        comment="A brief description of the plan, hidden from customers",
        nullable=True,
    ),
    Column(
        "object",
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    ),
    Column(
        "product",
        Product,
        ForeignKey("DeletedProduct"),
        comment="The product whose pricing this plan determines",
        nullable=True,
    ),
    Column(
        "tiers",
        list,
        comment="Each element represents a pricing tier. This parameter requires `billing_scheme` to be set to `tiered`. See also the documentation for `billing_scheme`",
        nullable=True,
    ),
    Column(
        "tiers_mode",
        String,
        comment="Defines if the tiering price should be `graduated` or `volume` based. In `volume`-based tiering, the maximum quantity within a period determines the per unit price. In `graduated` tiering, pricing can change as the quantity grows",
        nullable=True,
    ),
    Column(
        "transform_usage",
        TransformUsage,
        ForeignKey("TransformUsage"),
        comment="Apply a transformation to the reported usage or set quantity before computing the amount billed. Cannot be combined with `tiers`",
        nullable=True,
    ),
    Column(
        "trial_period_days",
        Integer,
        comment="Default number of trial days when subscribing a customer to this plan using [`trial_from_plan=true`](https://stripe.com/docs/api#create_subscription-trial_from_plan)",
        nullable=True,
    ),
    Column(
        "usage_type",
        String,
        comment="Configures how the quantity per period should be determined. Can be either `metered` or `licensed`. `licensed` automatically bills the `quantity` set when adding it to a subscription. `metered` aggregates the total usage based on usage records. Defaults to `licensed`",
    ),
)
__all__ = ["plan.json"]
