from sqlalchemy import Column, String

class Payment_Method_Boleto(Base):
    __tablename__ = 'payment_method_boleto'
    tax_id = Column(String, comment='Uniquely identifies the customer tax id (CNPJ or CPF)', primary_key=True)

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Payment_Method_Boleto(tax_id={tax_id!r})'.format(tax_id=self.tax_id)
__all__ = ['payment_method_boleto']