from sqlalchemy import Column, Integer, String


class Invoice_Payment_Method_Options_Bancontact(Base):
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
        return "Invoice_Payment_Method_Options_Bancontact(preferred_language={preferred_language!r}, id={id!r})".format(
            preferred_language=self.preferred_language, id=self.id
        )


__all__ = ["invoice_payment_method_options_bancontact"]
