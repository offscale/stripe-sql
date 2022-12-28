from sqlalchemy import Column, Integer

class Coupon_Currency_Option(Base):
    __tablename__ = 'coupon_currency_option'
    amount_off = Column(Integer, comment='Amount (in the `currency` specified) that will be taken off the subtotal of any invoices for this customer')
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Coupon_Currency_Option(amount_off={amount_off!r}, id={id!r})'.format(amount_off=self.amount_off, id=self.id)
__all__ = ['coupon_currency_option']