from sqlalchemy import Boolean, Column, Integer, String


class Price(Base):
    """
    Prices define the unit cost, currency, and (optional) billing cycle for both recurring and one-time purchases of products.

    [Products](https://stripe.com/docs/api#products) help you track inventory or provisioning, and prices help you track payment terms. Different physical goods or levels of service should be represented by products, and pricing options should be represented by prices. This approach lets you change prices without having to change your provisioning scheme.

    For example, you might have a single "gold" product that has prices for $10/month, $100/year, and €9 once.

    Related guides: [Set up a subscription](https://stripe.com/docs/billing/subscriptions/set-up-subscription), [create an invoice](https://stripe.com/docs/billing/invoices/create), and more about [products and prices](https://stripe.com/docs/products-prices/overview).

    """

    __tablename__ = "price"
    active = Column(Boolean, comment="Whether the price can be used for new purchases")
    billing_scheme = Column(
        String,
        comment="Describes how to compute the price per period. Either `per_unit` or `tiered`. `per_unit` indicates that the fixed amount (specified in `unit_amount` or `unit_amount_decimal`) will be charged per unit in `quantity` (for prices with `usage_type=licensed`), or per unit of total usage (for prices with `usage_type=metered`). `tiered` indicates that the unit pricing will be computed using a tiering strategy as defined using the `tiers` and `tiers_mode` attributes",
    )
    created = Column(
        Integer,
        comment="Time at which the object was created. Measured in seconds since the Unix epoch",
    )
    currency = Column(
        String,
        comment="Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)",
    )
    currency_options = Column(
        JSON,
        comment="Prices defined in each available currency option. Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies)",
        nullable=True,
    )
    custom_unit_amount = Column(
        custom_unit_amount,
        comment="[[FK(custom_unit_amount)]] When set, provides configuration for the amount to be adjusted by the customer during Checkout Sessions and Payment Links",
        nullable=True,
    )
    id = Column(String, comment="Unique identifier for the object", primary_key=True)
    livemode = Column(
        Boolean,
        comment="Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode",
    )
    lookup_key = Column(
        String,
        comment="A lookup key used to retrieve prices dynamically from a static string. This may be up to 200 characters",
        nullable=True,
    )
    metadata = Column(
        JSON,
        comment="Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format",
    )
    nickname = Column(
        String,
        comment="A brief description of the price, hidden from customers",
        nullable=True,
    )
    object = Column(
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    )
    product = Column(
        string | product,
        comment="[[FK(deleted_product)]] The ID of the product this price is associated with",
    )
    recurring = Column(
        recurring,
        comment="[[FK(recurring)]] The recurring components of a price such as `interval` and `usage_type`",
        nullable=True,
    )
    tax_behavior = Column(
        String,
        comment="Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed",
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
    transform_quantity = Column(
        transform_quantity,
        comment="[[FK(transform_quantity)]] Apply a transformation to the reported usage or set quantity before computing the amount billed. Cannot be combined with `tiers`",
        nullable=True,
    )
    type = Column(
        String,
        comment="One of `one_time` or `recurring` depending on whether the price is for a one-time purchase or a recurring (subscription) purchase",
    )
    unit_amount = Column(
        Integer,
        comment="The unit amount in %s to be charged, represented as a whole integer if possible. Only set if `billing_scheme=per_unit`",
        nullable=True,
    )
    unit_amount_decimal = Column(
        String,
        comment="The unit amount in %s to be charged, represented as a decimal string with at most 12 decimal places. Only set if `billing_scheme=per_unit`",
        nullable=True,
    )

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Price(active={active!r}, billing_scheme={billing_scheme!r}, created={created!r}, currency={currency!r}, currency_options={currency_options!r}, custom_unit_amount={custom_unit_amount!r}, id={id!r}, livemode={livemode!r}, lookup_key={lookup_key!r}, metadata={metadata!r}, nickname={nickname!r}, object={object!r}, product={product!r}, recurring={recurring!r}, tax_behavior={tax_behavior!r}, tiers={tiers!r}, tiers_mode={tiers_mode!r}, transform_quantity={transform_quantity!r}, type={type!r}, unit_amount={unit_amount!r}, unit_amount_decimal={unit_amount_decimal!r})".format(
            active=self.active,
            billing_scheme=self.billing_scheme,
            created=self.created,
            currency=self.currency,
            currency_options=self.currency_options,
            custom_unit_amount=self.custom_unit_amount,
            id=self.id,
            livemode=self.livemode,
            lookup_key=self.lookup_key,
            metadata=self.metadata,
            nickname=self.nickname,
            object=self.object,
            product=self.product,
            recurring=self.recurring,
            tax_behavior=self.tax_behavior,
            tiers=self.tiers,
            tiers_mode=self.tiers_mode,
            transform_quantity=self.transform_quantity,
            type=self.type,
            unit_amount=self.unit_amount,
            unit_amount_decimal=self.unit_amount_decimal,
        )


__all__ = ["price"]
