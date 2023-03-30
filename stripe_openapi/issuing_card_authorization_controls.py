from sqlalchemy import ARRAY, Column, Identity, Integer, String, Table, list

from . import metadata

IssuingCardAuthorizationControls.Json = Table(
    "issuing_card_authorization_controls.json",
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
        comment="Limit spending with amount-based rules that apply across any cards this card replaced (i.e., its `replacement_for` card and _that_ card's `replacement_for` card, up the chain)",
        nullable=True,
    ),
    Column(
        "spending_limits_currency",
        String,
        comment="Currency of the amounts within `spending_limits`. Always the same as the currency of the card",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["issuing_card_authorization_controls.json"]
