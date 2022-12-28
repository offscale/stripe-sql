from sqlalchemy import Column, Integer, String

class Level3(Base):
    __tablename__ = 'level3'
    customer_reference = Column(String, nullable=True)
    line_items = Column(list)
    merchant_reference = Column(String)
    shipping_address_zip = Column(String, nullable=True)
    shipping_amount = Column(Integer, nullable=True)
    shipping_from_zip = Column(String, nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Level3(customer_reference={customer_reference!r}, line_items={line_items!r}, merchant_reference={merchant_reference!r}, shipping_address_zip={shipping_address_zip!r}, shipping_amount={shipping_amount!r}, shipping_from_zip={shipping_from_zip!r}, id={id!r})'.format(customer_reference=self.customer_reference, line_items=self.line_items, merchant_reference=self.merchant_reference, shipping_address_zip=self.shipping_address_zip, shipping_amount=self.shipping_amount, shipping_from_zip=self.shipping_from_zip, id=self.id)
__all__ = ['level3']