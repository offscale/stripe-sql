from sqlalchemy import Column, ForeignKey, Identity, Integer, Table

from . import metadata

CustomerBalanceResourceCashBalanceTransactionResourceUnappliedFromPaymentTransactionJson = Table(
    "customer_balance_resource_cash_balance_transaction_resource_unapplied_from_payment_transactionjson",
    metadata,
    Column(
        "payment_intent",
        PaymentIntent,
        ForeignKey("PaymentIntent"),
        comment="The [Payment Intent](https://stripe.com/docs/api/payment_intents/object) that funds were unapplied from",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = [
    "customer_balance_resource_cash_balance_transaction_resource_unapplied_from_payment_transaction.json"
]
