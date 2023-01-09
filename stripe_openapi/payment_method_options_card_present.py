from sqlalchemy import Boolean, Column, Identity, Integer

from . import Base


class PaymentMethodOptionsCardPresent(Base):
    __tablename__ = "payment_method_options_card_present"
    request_extended_authorization = Column(
        Boolean,
        comment="Request ability to capture this payment beyond the standard [authorization validity window](https://stripe.com/docs/terminal/features/extended-authorizations#authorization-validity)",
        nullable=True,
    )
    request_incremental_authorization_support = Column(
        Boolean,
        comment="Request ability to [increment](https://stripe.com/docs/terminal/features/incremental-authorizations) this PaymentIntent if the combination of MCC and card brand is eligible. Check [incremental_authorization_supported](https://stripe.com/docs/api/charges/object#charge_object-payment_method_details-card_present-incremental_authorization_supported) in the [Confirm](https://stripe.com/docs/api/payment_intents/confirm) response to verify support",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "PaymentMethodOptionsCardPresent(request_extended_authorization={request_extended_authorization!r}, request_incremental_authorization_support={request_incremental_authorization_support!r}, id={id!r})".format(
            request_extended_authorization=self.request_extended_authorization,
            request_incremental_authorization_support=self.request_incremental_authorization_support,
            id=self.id,
        )


__all__ = ["payment_method_options_card_present"]
