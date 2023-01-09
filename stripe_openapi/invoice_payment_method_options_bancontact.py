from sqlalchemy import Column, Identity, Integer, String

from . import Base


class InvoicePaymentMethodOptionsBancontact(Base):
    __tablename__ = "invoice_payment_method_options_bancontact"
    preferred_language = Column(
        String,
        comment="Preferred language of the Bancontact authorization page that the customer is redirected to",
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "InvoicePaymentMethodOptionsBancontact(preferred_language={preferred_language!r}, id={id!r})".format(
            preferred_language=self.preferred_language, id=self.id
        )


__all__ = ["invoice_payment_method_options_bancontact"]
