from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table

from stripe_openapi.coupon import Coupon
from stripe_openapi.customer import Customer

from . import metadata

DeletedDiscountJson = Table(
    "deleted_discountjson",
    metadata,
    Column(
        "checkout_session",
        String,
        comment="The Checkout session that this coupon is applied to, if it is applied to a particular session in payment mode. Will not be present for subscription mode",
        nullable=True,
    ),
    Column("coupon", Coupon, ForeignKey("Coupon")),
    Column(
        "customer",
        Customer,
        ForeignKey("DeletedCustomer"),
        comment="The ID of the customer associated with this discount",
        nullable=True,
    ),
    Column("deleted", Boolean, comment="Always true for a deleted object"),
    Column(
        "id",
        String,
        comment="The ID of the discount object. Discounts cannot be fetched by ID. Use `expand[]=discounts` in API calls to expand discount IDs in an array",
        primary_key=True,
    ),
    Column(
        "invoice",
        String,
        comment="The invoice that the discount's coupon was applied to, if it was applied directly to a particular invoice",
        nullable=True,
    ),
    Column(
        "invoice_item",
        String,
        comment="The invoice item `id` (or invoice line item `id` for invoice line items of type='subscription') that the discount's coupon was applied to, if it was applied directly to a particular invoice item or invoice line item",
        nullable=True,
    ),
    Column(
        "object",
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    ),
    Column(
        "promotion_code",
        PromotionCode,
        ForeignKey("PromotionCode"),
        comment="The promotion code applied to create this discount",
        nullable=True,
    ),
    Column("start", Integer, comment="Date that the coupon was applied"),
    Column(
        "subscription",
        String,
        comment="The subscription that this coupon is applied to, if it is applied to a particular subscription",
        nullable=True,
    ),
)
__all__ = ["deleted_discount.json"]
