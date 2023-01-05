from sqlalchemy import Column, Integer, String


class Payment_Pages_Checkout_Session_Consent_Collection(Base):
    __tablename__ = "payment_pages_checkout_session_consent_collection"
    promotions = Column(
        String,
        comment="If set to `auto`, enables the collection of customer consent for promotional communications. The Checkout\nSession will determine whether to display an option to opt into promotional communication\nfrom the merchant depending on the customer's locale. Only available to US merchants",
        nullable=True,
    )
    terms_of_service = Column(
        String,
        comment="If set to `required`, it requires customers to accept the terms of service before being able to pay",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Payment_Pages_Checkout_Session_Consent_Collection(promotions={promotions!r}, terms_of_service={terms_of_service!r}, id={id!r})".format(
            promotions=self.promotions,
            terms_of_service=self.terms_of_service,
            id=self.id,
        )


__all__ = ["payment_pages_checkout_session_consent_collection"]
