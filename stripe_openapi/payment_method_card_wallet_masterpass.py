from sqlalchemy import Column, ForeignKey, Identity, Integer, String, Table

from stripe_openapi.address import Address

from . import metadata

PaymentMethodCardWalletMasterpassJson = Table(
    "payment_method_card_wallet_masterpassjson",
    metadata,
    Column(
        "billing_address",
        Address,
        ForeignKey("Address"),
        comment="Owner's verified billing address. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated",
        nullable=True,
    ),
    Column(
        "email",
        String,
        comment="Owner's verified email. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated",
        nullable=True,
    ),
    Column(
        "name",
        String,
        comment="Owner's verified full name. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated",
        nullable=True,
    ),
    Column(
        "shipping_address",
        Address,
        ForeignKey("Address"),
        comment="Owner's verified shipping address. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_method_card_wallet_masterpass.json"]
