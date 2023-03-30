from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

PaymentFlowsPrivatePaymentMethodsAlipay.Json = Table(
    "payment_flows_private_payment_methods_alipay.json",
    metadata,
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_flows_private_payment_methods_alipay.json"]
