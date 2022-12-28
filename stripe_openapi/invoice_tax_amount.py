from sqlalchemy import Boolean, Column, Integer

class Invoice_Tax_Amount(Base):
    __tablename__ = 'invoice_tax_amount'
    amount = Column(Integer, comment='The amount, in %s, of the tax')
    inclusive = Column(Boolean, comment='Whether this tax amount is inclusive or exclusive')
    tax_rate = Column(TaxRate, comment='The tax rate that was applied to get this tax amount')
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Invoice_Tax_Amount(amount={amount!r}, inclusive={inclusive!r}, tax_rate={tax_rate!r}, id={id!r})'.format(amount=self.amount, inclusive=self.inclusive, tax_rate=self.tax_rate, id=self.id)
__all__ = ['invoice_tax_amount']