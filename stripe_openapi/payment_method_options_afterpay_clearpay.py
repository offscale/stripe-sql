from sqlalchemy import Column, Identity, Integer, String

from . import Base


class PaymentMethodOptionsAfterpayClearpay(Base):
    __tablename__ = "payment_method_options_afterpay_clearpay"
    capture_method = Column(
        String,
        comment="Controls when the funds will be captured from the customer's account",
        nullable=True,
    )
    reference = Column(
        String,
        comment="Order identifier shown to the customer in Afterpay’s online portal. We recommend using a value that helps you answer any questions a customer might have about\nthe payment. The identifier is limited to 128 characters and may contain only letters, digits, underscores, backslashes and dashes",
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
        return "PaymentMethodOptionsAfterpayClearpay(capture_method={capture_method!r}, reference={reference!r}, setup_future_usage={setup_future_usage!r}, id={id!r})".format(
            capture_method=self.capture_method,
            reference=self.reference,
            setup_future_usage=self.setup_future_usage,
            id=self.id,
        )


__all__ = ["payment_method_options_afterpay_clearpay"]
