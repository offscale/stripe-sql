from sqlalchemy import ARRAY, Column, Identity, Integer, String, Table

from . import metadata

IssuingCardholderSpendingLimit.Json = Table(
    "issuing_cardholder_spending_limit.json",
    metadata,
    Column(
        "amount",
        Integer,
        comment="Maximum amount allowed to spend per interval. This amount is in the card's currency and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal)",
    ),
    Column(
        "categories",
        ARRAY(String),
        comment="Array of strings containing [categories](https://stripe.com/docs/api#issuing_authorization_object-merchant_data-category) this limit applies to. Omitting this field will apply the limit to all categories",
        nullable=True,
    ),
    Column(
        "interval", String, comment="Interval (or event) to which the amount applies"
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["issuing_cardholder_spending_limit.json"]
