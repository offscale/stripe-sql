from sqlalchemy import ARRAY, Column, Identity, Integer, String, Table, list

from . import metadata

IssuingCardholderAuthorizationControls.Json = Table(
    "issuing_cardholder_authorization_controls.json",
    metadata,
    Column(
        "allowed_categories",
        ARRAY(String),
        comment="Array of strings containing [categories](https://stripe.com/docs/api#issuing_authorization_object-merchant_data-category) of authorizations to allow. All other categories will be blocked. Cannot be set with `blocked_categories`",
        nullable=True,
    ),
    Column(
        "blocked_categories",
        ARRAY(String),
        comment="Array of strings containing [categories](https://stripe.com/docs/api#issuing_authorization_object-merchant_data-category) of authorizations to decline. All other categories will be allowed. Cannot be set with `allowed_categories`",
        nullable=True,
    ),
    Column(
        "spending_limits",
        list,
        comment="Limit spending with amount-based rules that apply across this cardholder's cards",
        nullable=True,
    ),
    Column(
        "spending_limits_currency",
        String,
        comment="Currency of the amounts within `spending_limits`",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["issuing_cardholder_authorization_controls.json"]
