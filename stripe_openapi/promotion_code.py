from sqlalchemy import JSON, Boolean, Column, ForeignKey, Integer, String, Table

from stripe_openapi.coupon import Coupon
from stripe_openapi.customer import Customer

from . import metadata

PromotionCode.Json = Table(
    "promotion_code.json",
    metadata,
    Column(
        "active",
        Boolean,
        comment="Whether the promotion code is currently active. A promotion code is only active if the coupon is also valid",
    ),
    Column(
        "code",
        String,
        comment="The customer-facing code. Regardless of case, this code must be unique across all active promotion codes for each customer",
    ),
    Column("coupon", Coupon, ForeignKey("Coupon")),
    Column(
        "created",
        Integer,
        comment="Time at which the object was created. Measured in seconds since the Unix epoch",
    ),
    Column(
        "customer",
        Customer,
        ForeignKey("DeletedCustomer"),
        comment="The customer that this promotion code can be used by",
        nullable=True,
    ),
    Column(
        "expires_at",
        Integer,
        comment="Date at which the promotion code can no longer be redeemed",
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
        comment="Maximum number of times this promotion code can be redeemed",
        nullable=True,
    ),
    Column(
        "metadata",
        JSON,
        comment="Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format",
        nullable=True,
    ),
    Column(
        "object",
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    ),
    Column(
        "restrictions",
        PromotionCodesResourceRestrictions,
        ForeignKey("PromotionCodesResourceRestrictions"),
    ),
    Column(
        "times_redeemed",
        Integer,
        comment="Number of times this promotion code has been used",
    ),
)
__all__ = ["promotion_code.json"]
