from sqlalchemy import JSON, Boolean, Column, ForeignKey, Integer, String, list

from . import Base


class Plan(Base):
    """
    You can now model subscriptions more flexibly using the [Prices API](https://stripe.com/docs/api#prices). It replaces the Plans API and is backwards compatible to simplify your migration.

    Plans define the base price, currency, and billing cycle for recurring purchases of products.
    [Products](https://stripe.com/docs/api#products) help you track inventory or provisioning, and plans help you track pricing. Different physical goods or levels of service should be represented by products, and pricing options should be represented by plans. This approach lets you change prices without having to change your provisioning scheme.

    For example, you might have a single "gold" product that has plans for $10/month, $100/year, €9/month, and €90/year.

    Related guides: [Set up a subscription](https://stripe.com/docs/billing/subscriptions/set-up-subscription) and more about [products and prices](https://stripe.com/docs/products-prices/overview).

    """

    __tablename__ = "plan"
    active = Column(Boolean, comment="Whether the plan can be used for new purchases")
    aggregate_usage = Column(
        String,
        comment="Specifies a usage aggregation strategy for plans of `usage_type=metered`. Allowed values are `sum` for summing up all usage during a period, `last_during_period` for using the last usage record reported within a period, `last_ever` for using the last usage record ever (across period bounds) or `max` which uses the usage record with the maximum reported usage during a period. Defaults to `sum`",
        nullable=True,
    )
    amount = Column(
        Integer,
        comment="The unit amount in %s to be charged, represented as a whole integer if possible. Only set if `billing_scheme=per_unit`",
        nullable=True,
    )
    amount_decimal = Column(
        String,
        comment="The unit amount in %s to be charged, represented as a decimal string with at most 12 decimal places. Only set if `billing_scheme=per_unit`",
        nullable=True,
    )
    billing_scheme = Column(
        String,
        comment="Describes how to compute the price per period. Either `per_unit` or `tiered`. `per_unit` indicates that the fixed amount (specified in `amount`) will be charged per unit in `quantity` (for plans with `usage_type=licensed`), or per unit of total usage (for plans with `usage_type=metered`). `tiered` indicates that the unit pricing will be computed using a tiering strategy as defined using the `tiers` and `tiers_mode` attributes",
    )
    created = Column(
        Integer,
        comment="Time at which the object was created. Measured in seconds since the Unix epoch",
    )
    currency = Column(
        String,
        comment="Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)",
    )
    id = Column(String, comment="Unique identifier for the object", primary_key=True)
    interval = Column(
        String,
        comment="The frequency at which a subscription is billed. One of `day`, `week`, `month` or `year`",
    )
    interval_count = Column(
        Integer,
        comment="The number of intervals (specified in the `interval` attribute) between subscription billings. For example, `interval=month` and `interval_count=3` bills every 3 months",
    )
    livemode = Column(
        Boolean,
        comment="Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode",
    )
    metadata = Column(
        JSON,
        comment="Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format",
        nullable=True,
    )
    nickname = Column(
        String,
        comment="A brief description of the plan, hidden from customers",
        nullable=True,
    )
    object = Column(
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    )
    product = Column(
        Product,
        ForeignKey("DeletedProduct"),
        comment="The product whose pricing this plan determines",
        nullable=True,
    )
    tiers = Column(
        list,
        comment="Each element represents a pricing tier. This parameter requires `billing_scheme` to be set to `tiered`. See also the documentation for `billing_scheme`",
        nullable=True,
    )
    tiers_mode = Column(
        String,
        comment="Defines if the tiering price should be `graduated` or `volume` based. In `volume`-based tiering, the maximum quantity within a period determines the per unit price. In `graduated` tiering, pricing can change as the quantity grows",
        nullable=True,
    )
    transform_usage = Column(
        Integer,
        ForeignKey("transform_usage.id"),
        comment="Apply a transformation to the reported usage or set quantity before computing the amount billed. Cannot be combined with `tiers`",
        nullable=True,
    )
    trial_period_days = Column(
        Integer,
        comment="Default number of trial days when subscribing a customer to this plan using [`trial_from_plan=true`](https://stripe.com/docs/api#create_subscription-trial_from_plan)",
        nullable=True,
    )
    usage_type = Column(
        String,
        comment="Configures how the quantity per period should be determined. Can be either `metered` or `licensed`. `licensed` automatically bills the `quantity` set when adding it to a subscription. `metered` aggregates the total usage based on usage records. Defaults to `licensed`",
    )

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Plan(active={active!r}, aggregate_usage={aggregate_usage!r}, amount={amount!r}, amount_decimal={amount_decimal!r}, billing_scheme={billing_scheme!r}, created={created!r}, currency={currency!r}, id={id!r}, interval={interval!r}, interval_count={interval_count!r}, livemode={livemode!r}, metadata={metadata!r}, nickname={nickname!r}, object={object!r}, product={product!r}, tiers={tiers!r}, tiers_mode={tiers_mode!r}, transform_usage={transform_usage!r}, trial_period_days={trial_period_days!r}, usage_type={usage_type!r})".format(
            active=self.active,
            aggregate_usage=self.aggregate_usage,
            amount=self.amount,
            amount_decimal=self.amount_decimal,
            billing_scheme=self.billing_scheme,
            created=self.created,
            currency=self.currency,
            id=self.id,
            interval=self.interval,
            interval_count=self.interval_count,
            livemode=self.livemode,
            metadata=self.metadata,
            nickname=self.nickname,
            object=self.object,
            product=self.product,
            tiers=self.tiers,
            tiers_mode=self.tiers_mode,
            transform_usage=self.transform_usage,
            trial_period_days=self.trial_period_days,
            usage_type=self.usage_type,
        )


__all__ = ["plan"]
