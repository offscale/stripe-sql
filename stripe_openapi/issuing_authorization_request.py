from sqlalchemy import Boolean, Column, Identity, Integer, String

from stripe_openapi.issuing_authorization_amount_details import (
    IssuingAuthorizationAmountDetails,
)

from . import Base


class IssuingAuthorizationRequest(Base):
    __tablename__ = "issuing_authorization_request"
    amount = Column(
        Integer,
        comment="The `pending_request.amount` at the time of the request, presented in your card's currency and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal). Stripe held this amount from your account to fund the authorization if the request was approved",
    )
    amount_details = Column(
        IssuingAuthorizationAmountDetails,
        comment="[[FK(IssuingAuthorizationAmountDetails)]] Detailed breakdown of amount components. These amounts are denominated in `currency` and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal)",
        nullable=True,
    )
    approved = Column(Boolean, comment="Whether this request was approved")
    created = Column(
        Integer,
        comment="Time at which the object was created. Measured in seconds since the Unix epoch",
    )
    currency = Column(
        String,
        comment="Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)",
    )
    merchant_amount = Column(
        Integer,
        comment="The `pending_request.merchant_amount` at the time of the request, presented in the `merchant_currency` and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal)",
    )
    merchant_currency = Column(
        String,
        comment="The currency that was collected by the merchant and presented to the cardholder for the authorization. Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)",
    )
    reason = Column(
        String,
        comment="When an authorization is approved or declined by you or by Stripe, this field provides additional detail on the reason for the outcome",
    )
    reason_message = Column(
        String,
        comment="If approve/decline decision is directly responsed to the webhook with json payload and if the response is invalid (e.g., parsing errors), we surface the detailed message via this field",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "IssuingAuthorizationRequest(amount={amount!r}, amount_details={amount_details!r}, approved={approved!r}, created={created!r}, currency={currency!r}, merchant_amount={merchant_amount!r}, merchant_currency={merchant_currency!r}, reason={reason!r}, reason_message={reason_message!r}, id={id!r})".format(
            amount=self.amount,
            amount_details=self.amount_details,
            approved=self.approved,
            created=self.created,
            currency=self.currency,
            merchant_amount=self.merchant_amount,
            merchant_currency=self.merchant_currency,
            reason=self.reason,
            reason_message=self.reason_message,
            id=self.id,
        )


__all__ = ["issuing_authorization_request"]
