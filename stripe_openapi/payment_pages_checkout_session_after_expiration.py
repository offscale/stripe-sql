from sqlalchemy import Column, Integer

class Payment_Pages_Checkout_Session_After_Expiration(Base):
    __tablename__ = 'payment_pages_checkout_session_after_expiration'
    recovery = Column(PaymentPagesCheckoutSessionAfterExpirationRecovery, comment='When set, configuration used to recover the Checkout Session on expiry', nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Payment_Pages_Checkout_Session_After_Expiration(recovery={recovery!r}, id={id!r})'.format(recovery=self.recovery, id=self.id)
__all__ = ['payment_pages_checkout_session_after_expiration']