from sqlalchemy import Column, ForeignKey, Identity, Integer, String, Table

from . import metadata

PaymentIntentPaymentMethodOptionsCardJson = Table(
    "payment_intent_payment_method_options_cardjson",
    metadata,
    Column(
        "capture_method",
        String,
        comment="Controls when the funds will be captured from the customer's account",
        nullable=True,
    ),
    Column(
        "installments",
        PaymentMethodOptionsCardInstallments,
        ForeignKey("PaymentMethodOptionsCardInstallments"),
        comment="Installment details for this payment (Mexico only).\n\nFor more information, see the [installments integration guide](https://stripe.com/docs/payments/installments)",
        nullable=True,
    ),
    Column(
        "mandate_options",
        PaymentMethodOptionsCardMandateOptions,
        ForeignKey("PaymentMethodOptionsCardMandateOptions"),
        comment="Configuration options for setting up an eMandate for cards issued in India",
        nullable=True,
    ),
    Column(
        "network",
        String,
        comment="Selected network to process this payment intent on. Depends on the available networks of the card attached to the payment intent. Can be only set confirm-time",
        nullable=True,
    ),
    Column(
        "request_three_d_secure",
        String,
        comment="We strongly recommend that you rely on our SCA Engine to automatically prompt your customers for authentication based on risk level and [other requirements](https://stripe.com/docs/strong-customer-authentication). However, if you wish to request 3D Secure based on logic from your own fraud engine, provide this option. Permitted values include: `automatic` or `any`. If not provided, defaults to `automatic`. Read our guide on [manually requesting 3D Secure](https://stripe.com/docs/payments/3d-secure#manual-three-ds) for more information on how this configuration interacts with Radar and our SCA Engine",
        nullable=True,
    ),
    Column(
        "setup_future_usage",
        String,
        comment="Indicates that you intend to make future payments with this PaymentIntent's payment method.\n\nProviding this parameter will [attach the payment method](https://stripe.com/docs/payments/save-during-payment) to the PaymentIntent's Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete. If no Customer was provided, the payment method can still be [attached](https://stripe.com/docs/api/payment_methods/attach) to a Customer after the transaction completes.\n\nWhen processing card payments, Stripe also uses `setup_future_usage` to dynamically optimize your payment flow and comply with regional legislation and network rules, such as [SCA](https://stripe.com/docs/strong-customer-authentication)",
        nullable=True,
    ),
    Column(
        "statement_descriptor_suffix_kana",
        String,
        comment="Provides information about a card payment that customers see on their statements. Concatenated with the Kana prefix (shortened Kana descriptor) or Kana statement descriptor that’s set on the account to form the complete statement descriptor. Maximum 22 characters. On card statements, the *concatenation* of both prefix and suffix (including separators) will appear truncated to 22 characters",
        nullable=True,
    ),
    Column(
        "statement_descriptor_suffix_kanji",
        String,
        comment="Provides information about a card payment that customers see on their statements. Concatenated with the Kanji prefix (shortened Kanji descriptor) or Kanji statement descriptor that’s set on the account to form the complete statement descriptor. Maximum 17 characters. On card statements, the *concatenation* of both prefix and suffix (including separators) will appear truncated to 17 characters",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_intent_payment_method_options_card.json"]
