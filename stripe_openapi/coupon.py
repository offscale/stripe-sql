from sqlalchemy import Boolean, Column, Float, Integer, String


class Coupon(Base):
    """
    A coupon contains information about a percent-off or amount-off discount you

    might want to apply to a customer. Coupons may be applied to [subscriptions](https://stripe.com/docs/api#subscriptions), [invoices](https://stripe.com/docs/api#invoices),
    [checkout sessions](https://stripe.com/docs/api/checkout/sessions), [quotes](https://stripe.com/docs/api#quotes), and more. Coupons do not work with conventional one-off [charges](https://stripe.com/docs/api#create_charge) or [payment intents](https://stripe.com/docs/api/payment_intents).

    """

    __tablename__ = "coupon"
    amount_off = Column(
        Integer,
        comment="Amount (in the `currency` specified) that will be taken off the subtotal of any invoices for this customer",
        nullable=True,
    )
    applies_to = Column(CouponAppliesTo, nullable=True)
    created = Column(
        Integer,
        comment="Time at which the object was created. Measured in seconds since the Unix epoch",
    )
    currency = Column(
        String,
        comment="If `amount_off` has been set, the three-letter [ISO code for the currency](https://stripe.com/docs/currencies) of the amount to take off",
        nullable=True,
    )
    currency_options = Column(
        JSON,
        comment="Coupons defined in each available currency option. Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies)",
        nullable=True,
    )
    duration = Column(
        String,
        comment="One of `forever`, `once`, and `repeating`. Describes how long a customer who applies this coupon will get the discount",
    )
    duration_in_months = Column(
        Integer,
        comment="If `duration` is `repeating`, the number of months the coupon applies. Null if coupon `duration` is `forever` or `once`",
        nullable=True,
    )
    id = Column(String, comment="Unique identifier for the object", primary_key=True)
    livemode = Column(
        Boolean,
        comment="Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode",
    )
    max_redemptions = Column(
        Integer,
        comment="Maximum number of times this coupon can be redeemed, in total, across all customers, before it is no longer valid",
        nullable=True,
    )
    metadata = Column(
        JSON,
        comment="Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format",
        nullable=True,
    )
    name = Column(
        String,
        comment="Name of the coupon displayed to customers on for instance invoices or receipts",
        nullable=True,
    )
    object = Column(
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    )
    percent_off = Column(
        Float,
        comment="Percent that will be taken off the subtotal of any invoices for this customer for the duration of the coupon. For example, a coupon with percent_off of 50 will make a %s100 invoice %s50 instead",
        nullable=True,
    )
    redeem_by = Column(
        Integer,
        comment="Date after which the coupon can no longer be redeemed",
        nullable=True,
    )
    times_redeemed = Column(
        Integer, comment="Number of times this coupon has been applied to a customer"
    )
    valid = Column(
        Boolean,
        comment="Taking account of the above properties, whether this coupon can still be applied to a customer",
    )

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Coupon(amount_off={amount_off!r}, applies_to={applies_to!r}, created={created!r}, currency={currency!r}, currency_options={currency_options!r}, duration={duration!r}, duration_in_months={duration_in_months!r}, id={id!r}, livemode={livemode!r}, max_redemptions={max_redemptions!r}, metadata={metadata!r}, name={name!r}, object={object!r}, percent_off={percent_off!r}, redeem_by={redeem_by!r}, times_redeemed={times_redeemed!r}, valid={valid!r})".format(
            amount_off=self.amount_off,
            applies_to=self.applies_to,
            created=self.created,
            currency=self.currency,
            currency_options=self.currency_options,
            duration=self.duration,
            duration_in_months=self.duration_in_months,
            id=self.id,
            livemode=self.livemode,
            max_redemptions=self.max_redemptions,
            metadata=self.metadata,
            name=self.name,
            object=self.object,
            percent_off=self.percent_off,
            redeem_by=self.redeem_by,
            times_redeemed=self.times_redeemed,
            valid=self.valid,
        )


__all__ = ["coupon"]
