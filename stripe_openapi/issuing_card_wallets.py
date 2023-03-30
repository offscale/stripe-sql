from sqlalchemy import Column, ForeignKey, String, Table

from . import metadata

IssuingCardWallets.Json = Table(
    "issuing_card_wallets.json",
    metadata,
    Column("apple_pay", IssuingCardApplePay, ForeignKey("IssuingCardApplePay")),
    Column("google_pay", IssuingCardGooglePay, ForeignKey("IssuingCardGooglePay")),
    Column(
        "primary_account_identifier",
        String,
        comment="Unique identifier for a card used with digital wallets",
        nullable=True,
        primary_key=True,
    ),
)
__all__ = ["issuing_card_wallets.json"]
