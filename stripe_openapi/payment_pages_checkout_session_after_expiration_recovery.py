from sqlalchemy import Boolean, Column, Integer, String

class Payment_Pages_Checkout_Session_After_Expiration_Recovery(Base):
    __tablename__ = 'payment_pages_checkout_session_after_expiration_recovery'
    allow_promotion_codes = Column(Boolean, comment='Enables user redeemable promotion codes on the recovered Checkout Sessions. Defaults to `false`')
    enabled = Column(Boolean, comment='If `true`, a recovery url will be generated to recover this Checkout Session if it\nexpires before a transaction is completed. It will be attached to the\nCheckout Session object upon expiration')
    expires_at = Column(Integer, comment='The timestamp at which the recovery URL will expire', nullable=True)
    url = Column(String, comment='URL that creates a new Checkout Session when clicked that is a copy of this expired Checkout Session', nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Payment_Pages_Checkout_Session_After_Expiration_Recovery(allow_promotion_codes={allow_promotion_codes!r}, enabled={enabled!r}, expires_at={expires_at!r}, url={url!r}, id={id!r})'.format(allow_promotion_codes=self.allow_promotion_codes, enabled=self.enabled, expires_at=self.expires_at, url=self.url, id=self.id)
__all__ = ['payment_pages_checkout_session_after_expiration_recovery']