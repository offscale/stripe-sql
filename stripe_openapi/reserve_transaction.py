from sqlalchemy import Column, Integer, String

class Reserve_Transaction(Base):
    __tablename__ = 'reserve_transaction'
    amount = Column(Integer)
    currency = Column(String, comment='Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)')
    description = Column(String, comment='An arbitrary string attached to the object. Often useful for displaying to users', nullable=True)
    id = Column(String, comment='Unique identifier for the object', primary_key=True)
    object = Column(String, comment="String representing the object's type. Objects of the same type share the same value")

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Reserve_Transaction(amount={amount!r}, currency={currency!r}, description={description!r}, id={id!r}, object={object!r})'.format(amount=self.amount, currency=self.currency, description=self.description, id=self.id, object=self.object)
__all__ = ['reserve_transaction']