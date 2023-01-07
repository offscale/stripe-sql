from sqlalchemy import Column, Integer, String


class Checkout_Card_Payment_Method_Options(Base):
    __tablename__ = "checkout_card_payment_method_options"
    installments = Column(
        checkout_card_installments_options,
        ForeignKey("checkout_card_installments_options"),
        nullable=True,
    )
    setup_future_usage = Column(
        String,
        comment="Indicates that you intend to make future payments with this PaymentIntent's payment method.\n\nProviding this parameter will [attach the payment method](https://stripe.com/docs/payments/save-during-payment) to the PaymentIntent's Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete. If no Customer was provided, the payment method can still be [attached](https://stripe.com/docs/api/payment_methods/attach) to a Customer after the transaction completes.\n\nWhen processing card payments, Stripe also uses `setup_future_usage` to dynamically optimize your payment flow and comply with regional legislation and network rules, such as [SCA](https://stripe.com/docs/strong-customer-authentication)",
        nullable=True,
    )
    statement_descriptor_suffix_kana = Column(
        String,
        comment="Provides information about a card payment that customers see on their statements. Concatenated with the Kana prefix (shortened Kana descriptor) or Kana statement descriptor that’s set on the account to form the complete statement descriptor. Maximum 22 characters. On card statements, the *concatenation* of both prefix and suffix (including separators) will appear truncated to 22 characters",
        nullable=True,
    )
    statement_descriptor_suffix_kanji = Column(
        String,
        comment="Provides information about a card payment that customers see on their statements. Concatenated with the Kanji prefix (shortened Kanji descriptor) or Kanji statement descriptor that’s set on the account to form the complete statement descriptor. Maximum 17 characters. On card statements, the *concatenation* of both prefix and suffix (including separators) will appear truncated to 17 characters",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Checkout_Card_Payment_Method_Options(installments={installments!r}, setup_future_usage={setup_future_usage!r}, statement_descriptor_suffix_kana={statement_descriptor_suffix_kana!r}, statement_descriptor_suffix_kanji={statement_descriptor_suffix_kanji!r}, id={id!r})".format(
            installments=self.installments,
            setup_future_usage=self.setup_future_usage,
            statement_descriptor_suffix_kana=self.statement_descriptor_suffix_kana,
            statement_descriptor_suffix_kanji=self.statement_descriptor_suffix_kanji,
            id=self.id,
        )


__all__ = ["checkout_card_payment_method_options"]
