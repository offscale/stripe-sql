from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

PaymentMethodDetailsStripeAccount.Json = Table(
    "payment_method_details_stripe_account.json",
    metadata,
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_method_details_stripe_account.json"]
