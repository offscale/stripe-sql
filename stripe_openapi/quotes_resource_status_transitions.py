from sqlalchemy import Column, Integer

class Quotes_Resource_Status_Transitions(Base):
    __tablename__ = 'quotes_resource_status_transitions'
    accepted_at = Column(Integer, comment='The time that the quote was accepted. Measured in seconds since Unix epoch', nullable=True)
    canceled_at = Column(Integer, comment='The time that the quote was canceled. Measured in seconds since Unix epoch', nullable=True)
    finalized_at = Column(Integer, comment='The time that the quote was finalized. Measured in seconds since Unix epoch', nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Quotes_Resource_Status_Transitions(accepted_at={accepted_at!r}, canceled_at={canceled_at!r}, finalized_at={finalized_at!r}, id={id!r})'.format(accepted_at=self.accepted_at, canceled_at=self.canceled_at, finalized_at=self.finalized_at, id=self.id)
__all__ = ['quotes_resource_status_transitions']