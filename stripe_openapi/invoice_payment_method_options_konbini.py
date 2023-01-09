from sqlalchemy import Column, Identity, Integer

from . import Base


class InvoicePaymentMethodOptionsKonbini(Base):
    __tablename__ = "invoice_payment_method_options_konbini"
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "InvoicePaymentMethodOptionsKonbini(id={id!r})".format(id=self.id)


__all__ = ["invoice_payment_method_options_konbini"]
