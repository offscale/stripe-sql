from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

PaymentMethodDetailsAfterpayClearpay.Json = Table(
    "payment_method_details_afterpay_clearpay.json",
    metadata,
    Column(
        "reference",
        String,
        comment="Order identifier shown to the merchant in Afterpay’s online portal",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_method_details_afterpay_clearpay.json"]
