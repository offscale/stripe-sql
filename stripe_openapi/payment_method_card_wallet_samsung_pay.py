from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

PaymentMethodCardWalletSamsungPay.Json = Table(
    "payment_method_card_wallet_samsung_pay.json",
    metadata,
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_method_card_wallet_samsung_pay.json"]
