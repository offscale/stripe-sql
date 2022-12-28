from sqlalchemy import Boolean, Column, Integer, String

class Payment_Pages_Checkout_Session_Automatic_Tax(Base):
    __tablename__ = 'payment_pages_checkout_session_automatic_tax'
    enabled = Column(Boolean, comment='Indicates whether automatic tax is enabled for the session')
    status = Column(String, comment='The status of the most recent automated tax calculation for this session', nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Payment_Pages_Checkout_Session_Automatic_Tax(enabled={enabled!r}, status={status!r}, id={id!r})'.format(enabled=self.enabled, status=self.status, id=self.id)
__all__ = ['payment_pages_checkout_session_automatic_tax']