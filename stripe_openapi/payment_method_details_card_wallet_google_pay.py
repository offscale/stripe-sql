from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

PaymentMethodDetailsCardWalletGooglePay.Json = Table(
    "payment_method_details_card_wallet_google_pay.json",
    metadata,
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_method_details_card_wallet_google_pay.json"]
