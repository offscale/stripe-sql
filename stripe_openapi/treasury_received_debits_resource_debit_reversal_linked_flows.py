from sqlalchemy import Column, Integer, String

class Treasury_Received_Debits_Resource_Debit_Reversal_Linked_Flows(Base):
    __tablename__ = 'treasury_received_debits_resource_debit_reversal_linked_flows'
    issuing_dispute = Column(String, comment='Set if there is an Issuing dispute associated with the DebitReversal', nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Treasury_Received_Debits_Resource_Debit_Reversal_Linked_Flows(issuing_dispute={issuing_dispute!r}, id={id!r})'.format(issuing_dispute=self.issuing_dispute, id=self.id)
__all__ = ['treasury_received_debits_resource_debit_reversal_linked_flows']