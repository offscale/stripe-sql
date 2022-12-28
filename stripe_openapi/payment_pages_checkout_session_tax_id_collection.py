from sqlalchemy import Boolean, Column, Integer

class Payment_Pages_Checkout_Session_Tax_Id_Collection(Base):
    __tablename__ = 'payment_pages_checkout_session_tax_id_collection'
    enabled = Column(Boolean, comment='Indicates whether tax ID collection is enabled for the session')
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Payment_Pages_Checkout_Session_Tax_Id_Collection(enabled={enabled!r}, id={id!r})'.format(enabled=self.enabled, id=self.id)
__all__ = ['payment_pages_checkout_session_tax_id_collection']