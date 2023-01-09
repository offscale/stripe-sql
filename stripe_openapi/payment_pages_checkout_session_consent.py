from sqlalchemy import Column, Identity, Integer, String

from . import Base


class PaymentPagesCheckoutSessionConsent(Base):
    __tablename__ = "payment_pages_checkout_session_consent"
    promotions = Column(
        String,
        comment="If `opt_in`, the customer consents to receiving promotional communications\nfrom the merchant about this Checkout Session",
        nullable=True,
    )
    terms_of_service = Column(
        String,
        comment="If `accepted`, the customer in this Checkout Session has agreed to the merchant's terms of service",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "PaymentPagesCheckoutSessionConsent(promotions={promotions!r}, terms_of_service={terms_of_service!r}, id={id!r})".format(
            promotions=self.promotions,
            terms_of_service=self.terms_of_service,
            id=self.id,
        )


__all__ = ["payment_pages_checkout_session_consent"]
