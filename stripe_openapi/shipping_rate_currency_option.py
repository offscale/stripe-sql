from sqlalchemy import Column, Integer, String

class Shipping_Rate_Currency_Option(Base):
    __tablename__ = 'shipping_rate_currency_option'
    amount = Column(Integer, comment='A non-negative integer in cents representing how much to charge')
    tax_behavior = Column(String, comment='Specifies whether the rate is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`')
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Shipping_Rate_Currency_Option(amount={amount!r}, tax_behavior={tax_behavior!r}, id={id!r})'.format(amount=self.amount, tax_behavior=self.tax_behavior, id=self.id)
__all__ = ['shipping_rate_currency_option']