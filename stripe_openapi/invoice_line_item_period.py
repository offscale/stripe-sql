from sqlalchemy import Column, Integer

class Invoice_Line_Item_Period(Base):
    __tablename__ = 'invoice_line_item_period'
    end = Column(Integer, comment='The end of the period, which must be greater than or equal to the start')
    start = Column(Integer, comment='The start of the period')
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Invoice_Line_Item_Period(end={end!r}, start={start!r}, id={id!r})'.format(end=self.end, start=self.start, id=self.id)
__all__ = ['invoice_line_item_period']