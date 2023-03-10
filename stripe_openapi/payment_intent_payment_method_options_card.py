from sqlalchemy import Column, ForeignKey, Identity, Integer, String

from . import Base


class PaymentIntentPaymentMethodOptionsCard(Base):
    __tablename__ = "payment_intent_payment_method_options_card"
    capture_method = Column(
        String,
        comment="Controls when the funds will be captured from the customer's account",
        nullable=True,
    )
    installments = Column(
        Integer,
        ForeignKey("payment_method_options_card_installments.id"),
        comment="Installment details for this payment (Mexico only).\n\nFor more information, see the [installments integration guide](https://stripe.com/docs/payments/installments)",
        nullable=True,
    )
    mandate_options = Column(
        Integer,
        ForeignKey("payment_method_options_card_mandate_options.id"),
        comment="Configuration options for setting up an eMandate for cards issued in India",
        nullable=True,
    )
    network = Column(
        String,
        comment="Selected network to process this payment intent on. Depends on the available networks of the card attached to the payment intent. Can be only set confirm-time",
        nullable=True,
    )
    request_three_d_secure = Column(
        String,
        comment="We strongly recommend that you rely on our SCA Engine to automatically prompt your customers for authentication based on risk level and [other requirements](https://stripe.com/docs/strong-customer-authentication). However, if you wish to request 3D Secure based on logic from your own fraud engine, provide this option. Permitted values include: `automatic` or `any`. If not provided, defaults to `automatic`. Read our guide on [manually requesting 3D Secure](https://stripe.com/docs/payments/3d-secure#manual-three-ds) for more information on how this configuration interacts with Radar and our SCA Engine",
        nullable=True,
    )
    setup_future_usage = Column(
        String,
        comment="Indicates that you intend to make future payments with this PaymentIntent's payment method.\n\nProviding this parameter will [attach the payment method](https://stripe.com/docs/payments/save-during-payment) to the PaymentIntent's Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete. If no Customer was provided, the payment method can still be [attached](https://stripe.com/docs/api/payment_methods/attach) to a Customer after the transaction completes.\n\nWhen processing card payments, Stripe also uses `setup_future_usage` to dynamically optimize your payment flow and comply with regional legislation and network rules, such as [SCA](https://stripe.com/docs/strong-customer-authentication)",
        nullable=True,
    )
    statement_descriptor_suffix_kana = Column(
        String,
        comment="Provides information about a card payment that customers see on their statements. Concatenated with the Kana prefix (shortened Kana descriptor) or Kana statement descriptor that???s set on the account to form the complete statement descriptor. Maximum 22 characters. On card statements, the *concatenation* of both prefix and suffix (including separators) will appear truncated to 22 characters",
        nullable=True,
    )
    statement_descriptor_suffix_kanji = Column(
        String,
        comment="Provides information about a card payment that customers see on their statements. Concatenated with the Kanji prefix (shortened Kanji descriptor) or Kanji statement descriptor that???s set on the account to form the complete statement descriptor. Maximum 17 characters. On card statements, the *concatenation* of both prefix and suffix (including separators) will appear truncated to 17 characters",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "PaymentIntentPaymentMethodOptionsCard(capture_method={capture_method!r}, installments={installments!r}, mandate_options={mandate_options!r}, network={network!r}, request_three_d_secure={request_three_d_secure!r}, setup_future_usage={setup_future_usage!r}, statement_descriptor_suffix_kana={statement_descriptor_suffix_kana!r}, statement_descriptor_suffix_kanji={statement_descriptor_suffix_kanji!r}, id={id!r})".format(
            capture_method=self.capture_method,
            installments=self.installments,
            mandate_options=self.mandate_options,
            network=self.network,
            request_three_d_secure=self.request_three_d_secure,
            setup_future_usage=self.setup_future_usage,
            statement_descriptor_suffix_kana=self.statement_descriptor_suffix_kana,
            statement_descriptor_suffix_kanji=self.statement_descriptor_suffix_kanji,
            id=self.id,
        )


__all__ = ["payment_intent_payment_method_options_card"]
