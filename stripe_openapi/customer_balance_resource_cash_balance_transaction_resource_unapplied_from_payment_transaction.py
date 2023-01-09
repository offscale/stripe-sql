from sqlalchemy import Column, Identity, Integer

from stripe_openapi.payment_intent import PaymentIntent

from . import Base


class CustomerBalanceResourceCashBalanceTransactionResourceUnappliedFromPaymentTransaction(
    Base
):
    __tablename__ = "customer_balance_resource_cash_balance_transaction_resource_unapplied_from_payment_transaction"
    payment_intent = Column(
        PaymentIntent,
        comment="[[FK(PaymentIntent)]] The [Payment Intent](https://stripe.com/docs/api/payment_intents/object) that funds were unapplied from",
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "CustomerBalanceResourceCashBalanceTransactionResourceUnappliedFromPaymentTransaction(payment_intent={payment_intent!r}, id={id!r})".format(
            payment_intent=self.payment_intent, id=self.id
        )


__all__ = [
    "customer_balance_resource_cash_balance_transaction_resource_unapplied_from_payment_transaction"
]
