from sqlalchemy import JSON, Boolean, Column, ForeignKey, Integer, String, Table, list

from stripe_openapi.product import Product
from stripe_openapi.recurring import Recurring

from . import metadata

PriceJson = Table(
    "pricejson",
    metadata,
    Column(
        "active", Boolean, comment="Whether the price can be used for new purchases"
    ),
    Column(
        "billing_scheme",
        String,
        comment="Describes how to compute the price per period. Either `per_unit` or `tiered`. `per_unit` indicates that the fixed amount (specified in `unit_amount` or `unit_amount_decimal`) will be charged per unit in `quantity` (for prices with `usage_type=licensed`), or per unit of total usage (for prices with `usage_type=metered`). `tiered` indicates that the unit pricing will be computed using a tiering strategy as defined using the `tiers` and `tiers_mode` attributes",
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
    Column(
        "currency_options",
        JSON,
        comment="Prices defined in each available currency option. Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies)",
        nullable=True,
    ),
    Column(
        "custom_unit_amount",
        CustomUnitAmount,
        ForeignKey("CustomUnitAmount"),
        comment="When set, provides configuration for the amount to be adjusted by the customer during Checkout Sessions and Payment Links",
        nullable=True,
    ),
    Column("id", String, comment="Unique identifier for the object", primary_key=True),
    Column(
        "livemode",
        Boolean,
        comment="Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode",
    ),
    Column(
        "lookup_key",
        String,
        comment="A lookup key used to retrieve prices dynamically from a static string. This may be up to 200 characters",
        nullable=True,
    ),
    Column(
        "metadata",
        JSON,
        comment="Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format",
    ),
    Column(
        "nickname",
        String,
        comment="A brief description of the price, hidden from customers",
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
        comment="The ID of the product this price is associated with",
    ),
    Column(
        "recurring",
        Recurring,
        ForeignKey("Recurring"),
        comment="The recurring components of a price such as `interval` and `usage_type`",
        nullable=True,
    ),
    Column(
        "tax_behavior",
        String,
        comment="Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed",
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
        "transform_quantity",
        TransformQuantity,
        ForeignKey("TransformQuantity"),
        comment="Apply a transformation to the reported usage or set quantity before computing the amount billed. Cannot be combined with `tiers`",
        nullable=True,
    ),
    Column(
        "type",
        String,
        comment="One of `one_time` or `recurring` depending on whether the price is for a one-time purchase or a recurring (subscription) purchase",
    ),
    Column(
        "unit_amount",
        Integer,
        comment="The unit amount in %s to be charged, represented as a whole integer if possible. Only set if `billing_scheme=per_unit`",
        nullable=True,
    ),
    Column(
        "unit_amount_decimal",
        String,
        comment="The unit amount in %s to be charged, represented as a decimal string with at most 12 decimal places. Only set if `billing_scheme=per_unit`",
        nullable=True,
    ),
)
__all__ = ["price.json"]
