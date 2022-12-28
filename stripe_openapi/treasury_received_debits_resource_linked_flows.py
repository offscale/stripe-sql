from sqlalchemy import Column, Integer, String

class Treasury_Received_Debits_Resource_Linked_Flows(Base):
    __tablename__ = 'treasury_received_debits_resource_linked_flows'
    debit_reversal = Column(String, comment='The DebitReversal created as a result of this ReceivedDebit being reversed', nullable=True)
    inbound_transfer = Column(String, comment="Set if the ReceivedDebit is associated with an InboundTransfer's return of funds", nullable=True)
    issuing_authorization = Column(String, comment='Set if the ReceivedDebit was created due to an [Issuing Authorization](https://stripe.com/docs/api#issuing_authorizations) object', nullable=True)
    issuing_transaction = Column(String, comment='Set if the ReceivedDebit is also viewable as an [Issuing Dispute](https://stripe.com/docs/api#issuing_disputes) object', nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Treasury_Received_Debits_Resource_Linked_Flows(debit_reversal={debit_reversal!r}, inbound_transfer={inbound_transfer!r}, issuing_authorization={issuing_authorization!r}, issuing_transaction={issuing_transaction!r}, id={id!r})'.format(debit_reversal=self.debit_reversal, inbound_transfer=self.inbound_transfer, issuing_authorization=self.issuing_authorization, issuing_transaction=self.issuing_transaction, id=self.id)
__all__ = ['treasury_received_debits_resource_linked_flows']