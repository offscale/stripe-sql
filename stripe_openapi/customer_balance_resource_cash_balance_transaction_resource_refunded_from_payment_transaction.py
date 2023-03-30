from sqlalchemy import Column, ForeignKey, Identity, Integer, Table

from stripe_openapi.refund import Refund

from . import metadata

CustomerBalanceResourceCashBalanceTransactionResourceRefundedFromPaymentTransaction.Json = Table(
    "customer_balance_resource_cash_balance_transaction_resource_refunded_from_payment_transaction.json",
    metadata,
    Column(
        "refund",
        Refund,
        ForeignKey("Refund"),
        comment="The [Refund](https://stripe.com/docs/api/refunds/object) that moved these funds into the customer's cash balance",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = [
    "customer_balance_resource_cash_balance_transaction_resource_refunded_from_payment_transaction.json"
]
