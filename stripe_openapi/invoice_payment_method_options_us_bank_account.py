from sqlalchemy import Column, Integer, String

class Invoice_Payment_Method_Options_Us_Bank_Account(Base):
    __tablename__ = 'invoice_payment_method_options_us_bank_account'
    financial_connections = Column(InvoicePaymentMethodOptionsUsBankAccountLinkedAccountOptions, nullable=True)
    verification_method = Column(String, comment='Bank account verification method', nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Invoice_Payment_Method_Options_Us_Bank_Account(financial_connections={financial_connections!r}, verification_method={verification_method!r}, id={id!r})'.format(financial_connections=self.financial_connections, verification_method=self.verification_method, id=self.id)
__all__ = ['invoice_payment_method_options_us_bank_account']