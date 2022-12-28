from sqlalchemy import Column, Integer, String

class Invoices_Line_Items_Credited_Items(Base):
    __tablename__ = 'invoices_line_items_credited_items'
    invoice = Column(String, comment='Invoice containing the credited invoice line items')
    invoice_line_items = Column(ARRAY(String), comment='Credited invoice line items')
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Invoices_Line_Items_Credited_Items(invoice={invoice!r}, invoice_line_items={invoice_line_items!r}, id={id!r})'.format(invoice=self.invoice, invoice_line_items=self.invoice_line_items, id=self.id)
__all__ = ['invoices_line_items_credited_items']