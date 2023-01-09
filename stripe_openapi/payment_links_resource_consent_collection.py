from sqlalchemy import Column, Identity, Integer, String

from . import Base


class PaymentLinksResourceConsentCollection(Base):
    __tablename__ = "payment_links_resource_consent_collection"
    promotions = Column(
        String,
        comment="If set to `auto`, enables the collection of customer consent for promotional communications",
        nullable=True,
    )
    terms_of_service = Column(
        String,
        comment="If set to `required`, it requires cutomers to accept the terms of service before being able to pay. If set to `none`, customers won't be shown a checkbox to accept the terms of service",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "PaymentLinksResourceConsentCollection(promotions={promotions!r}, terms_of_service={terms_of_service!r}, id={id!r})".format(
            promotions=self.promotions,
            terms_of_service=self.terms_of_service,
            id=self.id,
        )


__all__ = ["payment_links_resource_consent_collection"]
