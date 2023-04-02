from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

PaymentMethodDetailsCustomerBalanceJson = Table(
    "payment_method_details_customer_balancejson",
    metadata,
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_method_details_customer_balance.json"]
