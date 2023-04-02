from sqlalchemy import ARRAY, JSON, Boolean, Column, ForeignKey, Integer, String, Table

from stripe_openapi.price import Price

from . import metadata

ProductJson = Table(
    "productjson",
    metadata,
    Column(
        "active",
        Boolean,
        comment="Whether the product is currently available for purchase",
    ),
    Column(
        "attributes",
        ARRAY(String),
        comment='A list of up to 5 attributes that each SKU can provide values for (e.g., `["color", "size"]`)',
        nullable=True,
    ),
    Column(
        "caption",
        String,
        comment="A short one-line description of the product, meant to be displayable to the customer. Only applicable to products of `type=good`",
        nullable=True,
    ),
    Column(
        "created",
        Integer,
        comment="Time at which the object was created. Measured in seconds since the Unix epoch",
    ),
    Column(
        "deactivate_on",
        ARRAY(String),
        comment="An array of connect application identifiers that cannot purchase this product. Only applicable to products of `type=good`",
        nullable=True,
    ),
    Column(
        "default_price",
        Price,
        ForeignKey("Price"),
        comment="The ID of the [Price](https://stripe.com/docs/api/prices) object that is the default price for this product",
        nullable=True,
    ),
    Column(
        "description",
        String,
        comment="The product's description, meant to be displayable to the customer. Use this field to optionally store a long form explanation of the product being sold for your own rendering purposes",
        nullable=True,
    ),
    Column("id", String, comment="Unique identifier for the object", primary_key=True),
    Column(
        "images",
        ARRAY(String),
        comment="A list of up to 8 URLs of images for this product, meant to be displayable to the customer",
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
    ),
    Column(
        "name",
        String,
        comment="The product's name, meant to be displayable to the customer",
    ),
    Column(
        "object",
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    ),
    Column(
        "package_dimensions",
        PackageDimensions,
        ForeignKey("PackageDimensions"),
        comment="The dimensions of this product for shipping purposes",
        nullable=True,
    ),
    Column(
        "shippable",
        Boolean,
        comment="Whether this product is shipped (i.e., physical goods)",
        nullable=True,
    ),
    Column(
        "statement_descriptor",
        String,
        comment="Extra information about a product which will appear on your customer's credit card statement. In the case that multiple products are billed at once, the first statement descriptor will be used",
        nullable=True,
    ),
    Column(
        "tax_code",
        TaxCode,
        ForeignKey("TaxCode"),
        comment="A [tax code](https://stripe.com/docs/tax/tax-categories) ID",
        nullable=True,
    ),
    Column(
        "type",
        String,
        comment="The type of the product. The product is either of type `good`, which is eligible for use with Orders and SKUs, or `service`, which is eligible for use with Subscriptions and Plans",
    ),
    Column(
        "unit_label",
        String,
        comment="A label that represents units of this product. When set, this will be included in customers' receipts, invoices, Checkout, and the customer portal",
        nullable=True,
    ),
    Column(
        "updated",
        Integer,
        comment="Time at which the object was last updated. Measured in seconds since the Unix epoch",
    ),
    Column(
        "url",
        String,
        comment="A URL of a publicly-accessible webpage for this product",
        nullable=True,
    ),
)
__all__ = ["product.json"]
