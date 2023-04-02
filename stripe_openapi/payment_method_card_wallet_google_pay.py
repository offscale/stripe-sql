from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

PaymentMethodCardWalletGooglePayJson = Table(
    "payment_method_card_wallet_google_payjson",
    metadata,
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_method_card_wallet_google_pay.json"]
