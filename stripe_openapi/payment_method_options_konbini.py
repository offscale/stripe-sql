from sqlalchemy import Column, Integer, String


class Payment_Method_Options_Konbini(Base):
    __tablename__ = "payment_method_options_konbini"
    confirmation_number = Column(
        String,
        comment="An optional 10 to 11 digit numeric-only string determining the confirmation code at applicable convenience stores",
        nullable=True,
    )
    expires_after_days = Column(
        Integer,
        comment="The number of calendar days (between 1 and 60) after which Konbini payment instructions will expire. For example, if a PaymentIntent is confirmed with Konbini and `expires_after_days` set to 2 on Monday JST, the instructions will expire on Wednesday 23:59:59 JST",
        nullable=True,
    )
    expires_at = Column(
        Integer,
        comment="The timestamp at which the Konbini payment instructions will expire. Only one of `expires_after_days` or `expires_at` may be set",
        nullable=True,
    )
    product_description = Column(
        String,
        comment="A product descriptor of up to 22 characters, which will appear to customers at the convenience store",
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
        return "Payment_Method_Options_Konbini(confirmation_number={confirmation_number!r}, expires_after_days={expires_after_days!r}, expires_at={expires_at!r}, product_description={product_description!r}, setup_future_usage={setup_future_usage!r}, id={id!r})".format(
            confirmation_number=self.confirmation_number,
            expires_after_days=self.expires_after_days,
            expires_at=self.expires_at,
            product_description=self.product_description,
            setup_future_usage=self.setup_future_usage,
            id=self.id,
        )


__all__ = ["payment_method_options_konbini"]
