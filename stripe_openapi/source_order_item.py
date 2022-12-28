from sqlalchemy import Column, Integer, String

class Source_Order_Item(Base):
    __tablename__ = 'source_order_item'
    amount = Column(Integer, comment='The amount (price) for this order item', nullable=True)
    currency = Column(String, comment='This currency of this order item. Required when `amount` is present', nullable=True)
    description = Column(String, comment='Human-readable description for this order item', nullable=True)
    parent = Column(String, comment='The ID of the associated object for this line item. Expandable if not null (e.g., expandable to a SKU)', nullable=True)
    quantity = Column(Integer, comment='The quantity of this order item. When type is `sku`, this is the number of instances of the SKU to be ordered', nullable=True)
    type = Column(String, comment='The type of this order item. Must be `sku`, `tax`, or `shipping`', nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Source_Order_Item(amount={amount!r}, currency={currency!r}, description={description!r}, parent={parent!r}, quantity={quantity!r}, type={type!r}, id={id!r})'.format(amount=self.amount, currency=self.currency, description=self.description, parent=self.parent, quantity=self.quantity, type=self.type, id=self.id)
__all__ = ['source_order_item']