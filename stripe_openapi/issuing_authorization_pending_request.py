from sqlalchemy import Boolean, Column, ForeignKey, Identity, Integer, String, Table

from . import metadata

IssuingAuthorizationPendingRequest.Json = Table(
    "issuing_authorization_pending_request.json",
    metadata,
    Column(
        "amount",
        Integer,
        comment="The additional amount Stripe will hold if the authorization is approved, in the card's [currency](https://stripe.com/docs/api#issuing_authorization_object-pending-request-currency) and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal)",
    ),
    Column(
        "amount_details",
        IssuingAuthorizationAmountDetails,
        ForeignKey("IssuingAuthorizationAmountDetails"),
        comment="Detailed breakdown of amount components. These amounts are denominated in `currency` and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal)",
        nullable=True,
    ),
    Column(
        "currency",
        String,
        comment="Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)",
    ),
    Column(
        "is_amount_controllable",
        Boolean,
        comment="If set `true`, you may provide [amount](https://stripe.com/docs/api/issuing/authorizations/approve#approve_issuing_authorization-amount) to control how much to hold for the authorization",
    ),
    Column(
        "merchant_amount",
        Integer,
        comment="The amount the merchant is requesting to be authorized in the `merchant_currency`. The amount is in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal)",
    ),
    Column(
        "merchant_currency",
        String,
        comment="The local currency the merchant is requesting to authorize",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["issuing_authorization_pending_request.json"]
