from sqlalchemy import Column, Integer

class Invoices_Line_Items_Proration_Details(Base):
    __tablename__ = 'invoices_line_items_proration_details'
    credited_items = Column(InvoicesLineItemsCreditedItems, comment='For a credit proration `line_item`, the original debit line_items to which the credit proration applies', nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Invoices_Line_Items_Proration_Details(credited_items={credited_items!r}, id={id!r})'.format(credited_items=self.credited_items, id=self.id)
__all__ = ['invoices_line_items_proration_details']