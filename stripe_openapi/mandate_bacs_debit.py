from sqlalchemy import Column, Integer, String

class Mandate_Bacs_Debit(Base):
    __tablename__ = 'mandate_bacs_debit'
    network_status = Column(String, comment='The status of the mandate on the Bacs network. Can be one of `pending`, `revoked`, `refused`, or `accepted`')
    reference = Column(String, comment='The unique reference identifying the mandate on the Bacs network')
    url = Column(String, comment='The URL that will contain the mandate that the customer has signed')
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Mandate_Bacs_Debit(network_status={network_status!r}, reference={reference!r}, url={url!r}, id={id!r})'.format(network_status=self.network_status, reference=self.reference, url=self.url, id=self.id)
__all__ = ['mandate_bacs_debit']