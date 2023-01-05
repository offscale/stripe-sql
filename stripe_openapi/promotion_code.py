from sqlalchemy import Boolean, Column, Integer, String


class Promotion_Code(Base):
    """
    A Promotion Code represents a customer-redeemable code for a [coupon](https://stripe.com/docs/api#coupons). It can be used to

    create multiple codes for a single coupon.

    """

    __tablename__ = "promotion_code"
    active = Column(
        Boolean,
        comment="Whether the promotion code is currently active. A promotion code is only active if the coupon is also valid",
    )
    code = Column(
        String,
        comment="The customer-facing code. Regardless of case, this code must be unique across all active promotion codes for each customer",
    )
    coupon = Column(Coupon)
    created = Column(
        Integer,
        comment="Time at which the object was created. Measured in seconds since the Unix epoch",
    )
    customer = Column(
        string | Customer,
        comment="The customer that this promotion code can be used by",
        nullable=True,
    )
    expires_at = Column(
        Integer,
        comment="Date at which the promotion code can no longer be redeemed",
        nullable=True,
    )
    id = Column(String, comment="Unique identifier for the object", primary_key=True)
    livemode = Column(
        Boolean,
        comment="Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode",
    )
    max_redemptions = Column(
        Integer,
        comment="Maximum number of times this promotion code can be redeemed",
        nullable=True,
    )
    metadata = Column(
        JSON,
        comment="Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format",
        nullable=True,
    )
    object = Column(
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    )
    restrictions = Column(PromotionCodesResourceRestrictions)
    times_redeemed = Column(
        Integer, comment="Number of times this promotion code has been used"
    )

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Promotion_Code(active={active!r}, code={code!r}, coupon={coupon!r}, created={created!r}, customer={customer!r}, expires_at={expires_at!r}, id={id!r}, livemode={livemode!r}, max_redemptions={max_redemptions!r}, metadata={metadata!r}, object={object!r}, restrictions={restrictions!r}, times_redeemed={times_redeemed!r})".format(
            active=self.active,
            code=self.code,
            coupon=self.coupon,
            created=self.created,
            customer=self.customer,
            expires_at=self.expires_at,
            id=self.id,
            livemode=self.livemode,
            max_redemptions=self.max_redemptions,
            metadata=self.metadata,
            object=self.object,
            restrictions=self.restrictions,
            times_redeemed=self.times_redeemed,
        )


__all__ = ["promotion_code"]
