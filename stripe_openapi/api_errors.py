from sqlalchemy import Column, ForeignKey, Identity, Integer, String, Table

from . import metadata

ApiErrors.Json = Table(
    "api_errors.json",
    metadata,
    Column(
        "charge",
        String,
        comment="For card errors, the ID of the failed charge",
        nullable=True,
    ),
    Column(
        "code",
        String,
        comment="For some errors that could be handled programmatically, a short string indicating the [error code](https://stripe.com/docs/error-codes) reported",
        nullable=True,
    ),
    Column(
        "decline_code",
        String,
        comment="For card errors resulting from a card issuer decline, a short string indicating the [card issuer's reason for the decline](https://stripe.com/docs/declines#issuer-declines) if they provide one",
        nullable=True,
    ),
    Column(
        "doc_url",
        String,
        comment="A URL to more information about the [error code](https://stripe.com/docs/error-codes) reported",
        nullable=True,
    ),
    Column(
        "message",
        String,
        comment="A human-readable message providing more details about the error. For card errors, these messages can be shown to your users",
        nullable=True,
    ),
    Column(
        "param",
        String,
        comment="If the error is parameter-specific, the parameter related to the error. For example, you can use this to display a message near the correct form field",
        nullable=True,
    ),
    Column("payment_intent", PaymentIntent, ForeignKey("PaymentIntent"), nullable=True),
    Column("payment_method", PaymentMethod, ForeignKey("PaymentMethod"), nullable=True),
    Column(
        "payment_method_type",
        String,
        comment="If the error is specific to the type of payment method, the payment method type that had a problem. This field is only populated for invoice-related errors",
        nullable=True,
    ),
    Column(
        "request_log_url",
        String,
        comment="A URL to the request log entry in your dashboard",
        nullable=True,
    ),
    Column("setup_intent", SetupIntent, ForeignKey("SetupIntent"), nullable=True),
    Column("source", PaymentSource, ForeignKey("PaymentSource"), nullable=True),
    Column(
        "type",
        String,
        comment="The type of error returned. One of `api_error`, `card_error`, `idempotency_error`, or `invalid_request_error`",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["api_errors.json"]
