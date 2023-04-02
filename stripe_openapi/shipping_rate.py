from sqlalchemy import (
    JSON,
    Boolean,
    Column,
    ForeignKey,
    Identity,
    Integer,
    String,
    Table,
)

from . import metadata

ShippingRateJson = Table(
    "shipping_ratejson",
    metadata,
    Column(
        "active",
        Boolean,
        comment="Whether the shipping rate can be used for new purchases. Defaults to `true`",
    ),
    Column(
        "created",
        Integer,
        comment="Time at which the object was created. Measured in seconds since the Unix epoch",
    ),
    Column(
        "delivery_estimate",
        ShippingRateDeliveryEstimate,
        ForeignKey("ShippingRateDeliveryEstimate"),
        comment="The estimated range for how long shipping will take, meant to be displayable to the customer. This will appear on CheckoutSessions",
        nullable=True,
    ),
    Column(
        "display_name",
        String,
        comment="The name of the shipping rate, meant to be displayable to the customer. This will appear on CheckoutSessions",
        nullable=True,
    ),
    Column(
        "fixed_amount",
        ShippingRateFixedAmount,
        ForeignKey("ShippingRateFixedAmount"),
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
    Column(
        "livemode",
        Boolean,
        comment="Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode",
    ),
    Column(
        "metadata",
        JSON,
        comment="Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format",
    ),
    Column(
        "object",
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    ),
    Column(
        "tax_behavior",
        String,
        comment="Specifies whether the rate is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`",
        nullable=True,
    ),
    Column(
        "tax_code",
        TaxCode,
        ForeignKey("TaxCode"),
        comment="A [tax code](https://stripe.com/docs/tax/tax-categories) ID. The Shipping tax code is `txcd_92010001`",
        nullable=True,
    ),
    Column(
        "type",
        String,
        comment="The type of calculation to use on the shipping rate. Can only be `fixed_amount` for now",
    ),
)
__all__ = ["shipping_rate.json"]
