from sqlalchemy import Boolean, Column, Integer, String

class Ephemeral_Key(Base):
    __tablename__ = 'ephemeral_key'
    created = Column(Integer, comment='Time at which the object was created. Measured in seconds since the Unix epoch')
    expires = Column(Integer, comment='Time at which the key will expire. Measured in seconds since the Unix epoch')
    id = Column(String, comment='Unique identifier for the object', primary_key=True)
    livemode = Column(Boolean, comment='Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode')
    object = Column(String, comment="String representing the object's type. Objects of the same type share the same value")
    secret = Column(String, comment="The key's secret. You can use this value to make authorized requests to the Stripe API", nullable=True)

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Ephemeral_Key(created={created!r}, expires={expires!r}, id={id!r}, livemode={livemode!r}, object={object!r}, secret={secret!r})'.format(created=self.created, expires=self.expires, id=self.id, livemode=self.livemode, object=self.object, secret=self.secret)
__all__ = ['ephemeral_key']