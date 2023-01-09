from sqlalchemy import Column, Identity, Integer, String

from . import Base


class PaymentIntentPaymentMethodOptionsLink(Base):
    __tablename__ = "payment_intent_payment_method_options_link"
    capture_method = Column(
        String,
        comment="Controls when the funds will be captured from the customer's account",
        nullable=True,
    )
    persistent_token = Column(
        String, comment="Token used for persistent Link logins", nullable=True
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
        return "PaymentIntentPaymentMethodOptionsLink(capture_method={capture_method!r}, persistent_token={persistent_token!r}, setup_future_usage={setup_future_usage!r}, id={id!r})".format(
            capture_method=self.capture_method,
            persistent_token=self.persistent_token,
            setup_future_usage=self.setup_future_usage,
            id=self.id,
        )


__all__ = ["payment_intent_payment_method_options_link"]
