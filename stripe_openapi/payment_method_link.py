from sqlalchemy import Column, Integer, String

class Payment_Method_Link(Base):
    __tablename__ = 'payment_method_link'
    email = Column(String, comment="Account owner's email address", nullable=True)
    persistent_token = Column(String, comment='Token used for persistent Link logins', nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Payment_Method_Link(email={email!r}, persistent_token={persistent_token!r}, id={id!r})'.format(email=self.email, persistent_token=self.persistent_token, id=self.id)
__all__ = ['payment_method_link']