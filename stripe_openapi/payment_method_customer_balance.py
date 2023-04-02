from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

PaymentMethodCustomerBalanceJson = Table(
    "payment_method_customer_balancejson",
    metadata,
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_method_customer_balance.json"]
