from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

PaymentMethodDetailsCardWalletAmexExpressCheckoutJson = Table(
    "payment_method_details_card_wallet_amex_express_checkoutjson",
    metadata,
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_method_details_card_wallet_amex_express_checkout.json"]
