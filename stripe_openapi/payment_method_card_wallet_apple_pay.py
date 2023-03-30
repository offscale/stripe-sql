from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

PaymentMethodCardWalletApplePay.Json = Table(
    "payment_method_card_wallet_apple_pay.json",
    metadata,
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_method_card_wallet_apple_pay.json"]
