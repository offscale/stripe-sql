from sqlalchemy import Column, Integer, String

class Source_Transaction_Ach_Credit_Transfer_Data(Base):
    __tablename__ = 'source_transaction_ach_credit_transfer_data'
    customer_data = Column(String, comment='Customer data associated with the transfer', nullable=True)
    fingerprint = Column(String, comment='Bank account fingerprint associated with the transfer', nullable=True)
    last4 = Column(String, comment='Last 4 digits of the account number associated with the transfer', nullable=True)
    routing_number = Column(String, comment='Routing number associated with the transfer', nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Source_Transaction_Ach_Credit_Transfer_Data(customer_data={customer_data!r}, fingerprint={fingerprint!r}, last4={last4!r}, routing_number={routing_number!r}, id={id!r})'.format(customer_data=self.customer_data, fingerprint=self.fingerprint, last4=self.last4, routing_number=self.routing_number, id=self.id)
__all__ = ['source_transaction_ach_credit_transfer_data']