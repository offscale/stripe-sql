from sqlalchemy import Boolean, Column, Identity, Integer, Table

from . import metadata

PaymentMethodOptionsCardPresent.Json = Table(
    "payment_method_options_card_present.json",
    metadata,
    Column(
        "request_extended_authorization",
        Boolean,
        comment="Request ability to capture this payment beyond the standard [authorization validity window](https://stripe.com/docs/terminal/features/extended-authorizations#authorization-validity)",
        nullable=True,
    ),
    Column(
        "request_incremental_authorization_support",
        Boolean,
        comment="Request ability to [increment](https://stripe.com/docs/terminal/features/incremental-authorizations) this PaymentIntent if the combination of MCC and card brand is eligible. Check [incremental_authorization_supported](https://stripe.com/docs/api/charges/object#charge_object-payment_method_details-card_present-incremental_authorization_supported) in the [Confirm](https://stripe.com/docs/api/payment_intents/confirm) response to verify support",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_method_options_card_present.json"]
