from sqlalchemy import Boolean, Column, ForeignKey, Identity, Integer, String, Table

from . import metadata

IssuingAuthorizationRequest.Json = Table(
    "issuing_authorization_request.json",
    metadata,
    Column(
        "amount",
        Integer,
        comment="The `pending_request.amount` at the time of the request, presented in your card's currency and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal). Stripe held this amount from your account to fund the authorization if the request was approved",
    ),
    Column(
        "amount_details",
        IssuingAuthorizationAmountDetails,
        ForeignKey("IssuingAuthorizationAmountDetails"),
        comment="Detailed breakdown of amount components. These amounts are denominated in `currency` and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal)",
        nullable=True,
    ),
    Column("approved", Boolean, comment="Whether this request was approved"),
    Column(
        "created",
        Integer,
        comment="Time at which the object was created. Measured in seconds since the Unix epoch",
    ),
    Column(
        "currency",
        String,
        comment="Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)",
    ),
    Column(
        "merchant_amount",
        Integer,
        comment="The `pending_request.merchant_amount` at the time of the request, presented in the `merchant_currency` and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal)",
    ),
    Column(
        "merchant_currency",
        String,
        comment="The currency that was collected by the merchant and presented to the cardholder for the authorization. Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)",
    ),
    Column(
        "reason",
        String,
        comment="When an authorization is approved or declined by you or by Stripe, this field provides additional detail on the reason for the outcome",
    ),
    Column(
        "reason_message",
        String,
        comment="If approve/decline decision is directly responsed to the webhook with json payload and if the response is invalid (e.g., parsing errors), we surface the detailed message via this field",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["issuing_authorization_request.json"]
