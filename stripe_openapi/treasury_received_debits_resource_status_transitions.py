from sqlalchemy import Column, Integer

class Treasury_Received_Debits_Resource_Status_Transitions(Base):
    __tablename__ = 'treasury_received_debits_resource_status_transitions'
    completed_at = Column(Integer, comment='Timestamp describing when the DebitReversal changed status to `completed`', nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Treasury_Received_Debits_Resource_Status_Transitions(completed_at={completed_at!r}, id={id!r})'.format(completed_at=self.completed_at, id=self.id)
__all__ = ['treasury_received_debits_resource_status_transitions']