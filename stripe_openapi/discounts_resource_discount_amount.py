from sqlalchemy import Column, Integer

class Discounts_Resource_Discount_Amount(Base):
    __tablename__ = 'discounts_resource_discount_amount'
    amount = Column(Integer, comment='The amount, in %s, of the discount')
    discount = Column(string | Discount, comment='The discount that was applied to get this discount amount')
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Discounts_Resource_Discount_Amount(amount={amount!r}, discount={discount!r}, id={id!r})'.format(amount=self.amount, discount=self.discount, id=self.id)
__all__ = ['discounts_resource_discount_amount']