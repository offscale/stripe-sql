from sqlalchemy import Boolean, Column, Integer

class Portal_Invoice_List(Base):
    __tablename__ = 'portal_invoice_list'
    enabled = Column(Boolean, comment='Whether the feature is enabled')
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Portal_Invoice_List(enabled={enabled!r}, id={id!r})'.format(enabled=self.enabled, id=self.id)
__all__ = ['portal_invoice_list']