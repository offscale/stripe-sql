from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

PaymentMethodDetailsCustomerBalance.Json = Table(
    "payment_method_details_customer_balance.json",
    metadata,
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_method_details_customer_balance.json"]
