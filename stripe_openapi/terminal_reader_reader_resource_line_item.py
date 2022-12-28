from sqlalchemy import Column, Integer, String

class Terminal_Reader_Reader_Resource_Line_Item(Base):
    """
    Represents a line item to be displayed on the reader
        """
    __tablename__ = 'terminal_reader_reader_resource_line_item'
    amount = Column(Integer, comment='The amount of the line item. A positive integer in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal)')
    description = Column(String, comment='Description of the line item')
    quantity = Column(Integer, comment='The quantity of the line item')
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Terminal_Reader_Reader_Resource_Line_Item(amount={amount!r}, description={description!r}, quantity={quantity!r}, id={id!r})'.format(amount=self.amount, description=self.description, quantity=self.quantity, id=self.id)
__all__ = ['terminal_reader_reader_resource_line_item']