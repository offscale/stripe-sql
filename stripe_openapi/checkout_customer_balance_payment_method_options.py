from sqlalchemy import Column, Integer, String


class Checkout_Customer_Balance_Payment_Method_Options(Base):
    __tablename__ = "checkout_customer_balance_payment_method_options"
    bank_transfer = Column(
        checkout_customer_balance_bank_transfer_payment_method_options,
        ForeignKey("checkout_customer_balance_bank_transfer_payment_method_options"),
        nullable=True,
    )
    funding_type = Column(
        String,
        comment="The funding method type to be used when there are not enough funds in the customer balance. Permitted values include: `bank_transfer`",
        nullable=True,
    )
    setup_future_usage = Column(
        String,
        comment="Indicates that you intend to make future payments with this PaymentIntent's payment method.\n\nProviding this parameter will [attach the payment method](https://stripe.com/docs/payments/save-during-payment) to the PaymentIntent's Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete. If no Customer was provided, the payment method can still be [attached](https://stripe.com/docs/api/payment_methods/attach) to a Customer after the transaction completes.\n\nWhen processing card payments, Stripe also uses `setup_future_usage` to dynamically optimize your payment flow and comply with regional legislation and network rules, such as [SCA](https://stripe.com/docs/strong-customer-authentication)",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Checkout_Customer_Balance_Payment_Method_Options(bank_transfer={bank_transfer!r}, funding_type={funding_type!r}, setup_future_usage={setup_future_usage!r}, id={id!r})".format(
            bank_transfer=self.bank_transfer,
            funding_type=self.funding_type,
            setup_future_usage=self.setup_future_usage,
            id=self.id,
        )


__all__ = ["checkout_customer_balance_payment_method_options"]
