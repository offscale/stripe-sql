from sqlalchemy import JSON, Boolean, Column, Float, Identity, Integer, String, Table

from . import metadata

TaxRate.Json = Table(
    "tax_rate.json",
    metadata,
    Column(
        "active",
        Boolean,
        comment="Defaults to `true`. When set to `false`, this tax rate cannot be used with new applications or Checkout Sessions, but will still work for subscriptions and invoices that already have it set",
    ),
    Column(
        "country",
        String,
        comment="Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2))",
        nullable=True,
    ),
    Column(
        "created",
        Integer,
        comment="Time at which the object was created. Measured in seconds since the Unix epoch",
    ),
    Column(
        "description",
        String,
        comment="An arbitrary string attached to the tax rate for your internal use only. It will not be visible to your customers",
        nullable=True,
    ),
    Column(
        "display_name",
        String,
        comment="The display name of the tax rates as it will appear to your customer on their receipt email, PDF, and the hosted invoice page",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
    Column(
        "inclusive",
        Boolean,
        comment="This specifies if the tax rate is inclusive or exclusive",
    ),
    Column(
        "jurisdiction",
        String,
        comment="The jurisdiction for the tax rate. You can use this label field for tax reporting purposes. It also appears on your customer’s invoice",
        nullable=True,
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
        "object",
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    ),
    Column(
        "percentage", Float, comment="This represents the tax rate percent out of 100"
    ),
    Column(
        "state",
        String,
        comment='[ISO 3166-2 subdivision code](https://en.wikipedia.org/wiki/ISO_3166-2:US), without country prefix. For example, "NY" for New York, United States',
        nullable=True,
    ),
    Column(
        "tax_type",
        String,
        comment="The high-level tax type, such as `vat` or `sales_tax`",
        nullable=True,
    ),
)
__all__ = ["tax_rate.json"]
