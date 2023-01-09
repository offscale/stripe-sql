from sqlalchemy import Column, ForeignKey, Identity, Integer, String

from . import Base


class InvoicePaymentMethodOptionsAcssDebit(Base):
    __tablename__ = "invoice_payment_method_options_acss_debit"
    mandate_options = Column(
        Integer,
        ForeignKey("invoice_payment_method_options_acss_debit_mandate_options.id"),
        nullable=True,
    )
    verification_method = Column(
        String, comment="Bank account verification method", nullable=True
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "InvoicePaymentMethodOptionsAcssDebit(mandate_options={mandate_options!r}, verification_method={verification_method!r}, id={id!r})".format(
            mandate_options=self.mandate_options,
            verification_method=self.verification_method,
            id=self.id,
        )


__all__ = ["invoice_payment_method_options_acss_debit"]
