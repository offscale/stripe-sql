from sqlalchemy import Column, Integer, String

class Invoice_Mandate_Options_Card(Base):
    __tablename__ = 'invoice_mandate_options_card'
    amount = Column(Integer, comment='Amount to be charged for future payments', nullable=True)
    amount_type = Column(String, comment='One of `fixed` or `maximum`. If `fixed`, the `amount` param refers to the exact amount to be charged in future payments. If `maximum`, the amount charged can be up to the value passed for the `amount` param', nullable=True)
    description = Column(String, comment='A description of the mandate or subscription that is meant to be displayed to the customer', nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Invoice_Mandate_Options_Card(amount={amount!r}, amount_type={amount_type!r}, description={description!r}, id={id!r})'.format(amount=self.amount, amount_type=self.amount_type, description=self.description, id=self.id)
__all__ = ['invoice_mandate_options_card']