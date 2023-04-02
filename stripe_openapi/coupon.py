from sqlalchemy import JSON, Boolean, Column, Float, ForeignKey, Integer, String, Table

from . import metadata

CouponJson = Table(
    "couponjson",
    metadata,
    Column(
        "amount_off",
        Integer,
        comment="Amount (in the `currency` specified) that will be taken off the subtotal of any invoices for this customer",
        nullable=True,
    ),
    Column("applies_to", CouponAppliesTo, ForeignKey("CouponAppliesTo"), nullable=True),
    Column(
        "created",
        Integer,
        comment="Time at which the object was created. Measured in seconds since the Unix epoch",
    ),
    Column(
        "currency",
        String,
        comment="If `amount_off` has been set, the three-letter [ISO code for the currency](https://stripe.com/docs/currencies) of the amount to take off",
        nullable=True,
    ),
    Column(
        "currency_options",
        JSON,
        comment="Coupons defined in each available currency option. Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies)",
        nullable=True,
    ),
    Column(
        "duration",
        String,
        comment="One of `forever`, `once`, and `repeating`. Describes how long a customer who applies this coupon will get the discount",
    ),
    Column(
        "duration_in_months",
        Integer,
        comment="If `duration` is `repeating`, the number of months the coupon applies. Null if coupon `duration` is `forever` or `once`",
        nullable=True,
    ),
    Column("id", String, comment="Unique identifier for the object", primary_key=True),
    Column(
        "livemode",
        Boolean,
        comment="Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode",
    ),
    Column(
        "max_redemptions",
        Integer,
        comment="Maximum number of times this coupon can be redeemed, in total, across all customers, before it is no longer valid",
        nullable=True,
    ),
    Column(
        "metadata",
        JSON,
        comment="Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format",
        nullable=True,
    ),
    Column(
        "name",
        String,
        comment="Name of the coupon displayed to customers on for instance invoices or receipts",
        nullable=True,
    ),
    Column(
        "object",
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    ),
    Column(
        "percent_off",
        Float,
        comment="Percent that will be taken off the subtotal of any invoices for this customer for the duration of the coupon. For example, a coupon with percent_off of 50 will make a %s100 invoice %s50 instead",
        nullable=True,
    ),
    Column(
        "redeem_by",
        Integer,
        comment="Date after which the coupon can no longer be redeemed",
        nullable=True,
    ),
    Column(
        "times_redeemed",
        Integer,
        comment="Number of times this coupon has been applied to a customer",
    ),
    Column(
        "valid",
        Boolean,
        comment="Taking account of the above properties, whether this coupon can still be applied to a customer",
    ),
)
__all__ = ["coupon.json"]
