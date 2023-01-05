from sqlalchemy import Boolean, Column, Integer, String


class Shipping_Rate(Base):
    """
    Shipping rates describe the price of shipping presented to your customers and can be

    applied to [Checkout Sessions](https://stripe.com/docs/payments/checkout/shipping)
    and [Orders](https://stripe.com/docs/orders/shipping) to collect shipping costs.

    """

    __tablename__ = "shipping_rate"
    active = Column(
        Boolean,
        comment="Whether the shipping rate can be used for new purchases. Defaults to `true`",
    )
    created = Column(
        Integer,
        comment="Time at which the object was created. Measured in seconds since the Unix epoch",
    )
    delivery_estimate = Column(
        ShippingRateDeliveryEstimate,
        comment="The estimated range for how long shipping will take, meant to be displayable to the customer. This will appear on CheckoutSessions",
        nullable=True,
    )
    display_name = Column(
        String,
        comment="The name of the shipping rate, meant to be displayable to the customer. This will appear on CheckoutSessions",
        nullable=True,
    )
    fixed_amount = Column(ShippingRateFixedAmount, nullable=True)
    id = Column(String, comment="Unique identifier for the object", primary_key=True)
    livemode = Column(
        Boolean,
        comment="Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode",
    )
    metadata = Column(
        JSON,
        comment="Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format",
    )
    object = Column(
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    )
    tax_behavior = Column(
        String,
        comment="Specifies whether the rate is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`",
        nullable=True,
    )
    tax_code = Column(
        TaxCode,
        comment="A [tax code](https://stripe.com/docs/tax/tax-categories) ID. The Shipping tax code is `txcd_92010001`",
        nullable=True,
    )
    type = Column(
        String,
        comment="The type of calculation to use on the shipping rate. Can only be `fixed_amount` for now",
    )

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Shipping_Rate(active={active!r}, created={created!r}, delivery_estimate={delivery_estimate!r}, display_name={display_name!r}, fixed_amount={fixed_amount!r}, id={id!r}, livemode={livemode!r}, metadata={metadata!r}, object={object!r}, tax_behavior={tax_behavior!r}, tax_code={tax_code!r}, type={type!r})".format(
            active=self.active,
            created=self.created,
            delivery_estimate=self.delivery_estimate,
            display_name=self.display_name,
            fixed_amount=self.fixed_amount,
            id=self.id,
            livemode=self.livemode,
            metadata=self.metadata,
            object=self.object,
            tax_behavior=self.tax_behavior,
            tax_code=self.tax_code,
            type=self.type,
        )


__all__ = ["shipping_rate"]
