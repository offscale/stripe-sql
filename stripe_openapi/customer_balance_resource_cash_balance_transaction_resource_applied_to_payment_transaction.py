from sqlalchemy import Column, Integer


class Customer_Balance_Resource_Cash_Balance_Transaction_Resource_Applied_To_Payment_Transaction(
    Base
):
    __tablename__ = "customer_balance_resource_cash_balance_transaction_resource_applied_to_payment_transaction"
    payment_intent = Column(
        PaymentIntent,
        comment="The [Payment Intent](https://stripe.com/docs/api/payment_intents/object) that funds were applied to",
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Customer_Balance_Resource_Cash_Balance_Transaction_Resource_Applied_To_Payment_Transaction(payment_intent={payment_intent!r}, id={id!r})".format(
            payment_intent=self.payment_intent, id=self.id
        )


__all__ = [
    "customer_balance_resource_cash_balance_transaction_resource_applied_to_payment_transaction"
]
