from sqlalchemy import Column, ForeignKey, Identity, Integer, String, Table

from . import metadata

SetupIntentPaymentMethodOptionsCard.Json = Table(
    "setup_intent_payment_method_options_card.json",
    metadata,
    Column(
        "mandate_options",
        SetupIntentPaymentMethodOptionsCardMandateOptions,
        ForeignKey("SetupIntentPaymentMethodOptionsCardMandateOptions"),
        comment="Configuration options for setting up an eMandate for cards issued in India",
        nullable=True,
    ),
    Column(
        "network",
        String,
        comment="Selected network to process this SetupIntent on. Depends on the available networks of the card attached to the setup intent. Can be only set confirm-time",
        nullable=True,
    ),
    Column(
        "request_three_d_secure",
        String,
        comment="We strongly recommend that you rely on our SCA Engine to automatically prompt your customers for authentication based on risk level and [other requirements](https://stripe.com/docs/strong-customer-authentication). However, if you wish to request 3D Secure based on logic from your own fraud engine, provide this option. Permitted values include: `automatic` or `any`. If not provided, defaults to `automatic`. Read our guide on [manually requesting 3D Secure](https://stripe.com/docs/payments/3d-secure#manual-three-ds) for more information on how this configuration interacts with Radar and our SCA Engine",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["setup_intent_payment_method_options_card.json"]
