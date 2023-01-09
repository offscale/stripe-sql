from sqlalchemy import Column, Identity, Integer, String

from . import Base


class InvoicePaymentMethodOptionsAcssDebitMandateOptions(Base):
    __tablename__ = "invoice_payment_method_options_acss_debit_mandate_options"
    transaction_type = Column(
        String, comment="Transaction type of the mandate", nullable=True
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "InvoicePaymentMethodOptionsAcssDebitMandateOptions(transaction_type={transaction_type!r}, id={id!r})".format(
            transaction_type=self.transaction_type, id=self.id
        )


__all__ = ["invoice_payment_method_options_acss_debit_mandate_options"]
