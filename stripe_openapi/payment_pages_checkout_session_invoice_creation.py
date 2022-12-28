from sqlalchemy import Boolean, Column, Integer

class Payment_Pages_Checkout_Session_Invoice_Creation(Base):
    __tablename__ = 'payment_pages_checkout_session_invoice_creation'
    enabled = Column(Boolean, comment='Indicates whether invoice creation is enabled for the Checkout Session')
    invoice_data = Column(PaymentPagesCheckoutSessionInvoiceSettings)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Payment_Pages_Checkout_Session_Invoice_Creation(enabled={enabled!r}, invoice_data={invoice_data!r}, id={id!r})'.format(enabled=self.enabled, invoice_data=self.invoice_data, id=self.id)
__all__ = ['payment_pages_checkout_session_invoice_creation']