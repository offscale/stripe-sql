from sqlalchemy import Column, Integer, String

class Customer_Acceptance(Base):
    __tablename__ = 'customer_acceptance'
    accepted_at = Column(Integer, comment='The time at which the customer accepted the Mandate', nullable=True)
    offline = Column(OfflineAcceptance, nullable=True)
    online = Column(OnlineAcceptance, nullable=True)
    type = Column(String, comment='The type of customer acceptance information included with the Mandate. One of `online` or `offline`')
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Customer_Acceptance(accepted_at={accepted_at!r}, offline={offline!r}, online={online!r}, type={type!r}, id={id!r})'.format(accepted_at=self.accepted_at, offline=self.offline, online=self.online, type=self.type, id=self.id)
__all__ = ['customer_acceptance']