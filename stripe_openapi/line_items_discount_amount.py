from sqlalchemy import Column, Integer

class Line_Items_Discount_Amount(Base):
    __tablename__ = 'line_items_discount_amount'
    amount = Column(Integer, comment='The amount discounted')
    discount = Column(Discount)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Line_Items_Discount_Amount(amount={amount!r}, discount={discount!r}, id={id!r})'.format(amount=self.amount, discount=self.discount, id=self.id)
__all__ = ['line_items_discount_amount']