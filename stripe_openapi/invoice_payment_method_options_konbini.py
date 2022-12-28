from sqlalchemy import Column, Integer

class Invoice_Payment_Method_Options_Konbini(Base):
    __tablename__ = 'invoice_payment_method_options_konbini'
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Invoice_Payment_Method_Options_Konbini(id={id!r})'.format(id=self.id)
__all__ = ['invoice_payment_method_options_konbini']