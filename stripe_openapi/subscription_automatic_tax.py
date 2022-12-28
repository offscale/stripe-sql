from sqlalchemy import Boolean, Column, Integer

class Subscription_Automatic_Tax(Base):
    __tablename__ = 'subscription_automatic_tax'
    enabled = Column(Boolean, comment='Whether Stripe automatically computes tax on this subscription')
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Subscription_Automatic_Tax(enabled={enabled!r}, id={id!r})'.format(enabled=self.enabled, id=self.id)
__all__ = ['subscription_automatic_tax']