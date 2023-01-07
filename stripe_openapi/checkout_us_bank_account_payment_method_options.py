from sqlalchemy import Column, Integer, String


class Checkout_Us_Bank_Account_Payment_Method_Options(Base):
    __tablename__ = "checkout_us_bank_account_payment_method_options"
    financial_connections = Column(
        linked_account_options_us_bank_account,
        ForeignKey("linked_account_options_us_bank_account"),
        nullable=True,
    )
    setup_future_usage = Column(
        String,
        comment="Indicates that you intend to make future payments with this PaymentIntent's payment method.\n\nProviding this parameter will [attach the payment method](https://stripe.com/docs/payments/save-during-payment) to the PaymentIntent's Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete. If no Customer was provided, the payment method can still be [attached](https://stripe.com/docs/api/payment_methods/attach) to a Customer after the transaction completes.\n\nWhen processing card payments, Stripe also uses `setup_future_usage` to dynamically optimize your payment flow and comply with regional legislation and network rules, such as [SCA](https://stripe.com/docs/strong-customer-authentication)",
        nullable=True,
    )
    verification_method = Column(
        String, comment="Bank account verification method", nullable=True
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Checkout_Us_Bank_Account_Payment_Method_Options(financial_connections={financial_connections!r}, setup_future_usage={setup_future_usage!r}, verification_method={verification_method!r}, id={id!r})".format(
            financial_connections=self.financial_connections,
            setup_future_usage=self.setup_future_usage,
            verification_method=self.verification_method,
            id=self.id,
        )


__all__ = ["checkout_us_bank_account_payment_method_options"]
