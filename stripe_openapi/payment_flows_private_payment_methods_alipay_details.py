from sqlalchemy import Column, Integer, String

class Payment_Flows_Private_Payment_Methods_Alipay_Details(Base):
    __tablename__ = 'payment_flows_private_payment_methods_alipay_details'
    buyer_id = Column(String, comment='Uniquely identifies this particular Alipay account. You can use this attribute to check whether two Alipay accounts are the same', nullable=True)
    fingerprint = Column(String, comment='Uniquely identifies this particular Alipay account. You can use this attribute to check whether two Alipay accounts are the same', nullable=True)
    transaction_id = Column(String, comment='Transaction ID of this particular Alipay transaction', nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Payment_Flows_Private_Payment_Methods_Alipay_Details(buyer_id={buyer_id!r}, fingerprint={fingerprint!r}, transaction_id={transaction_id!r}, id={id!r})'.format(buyer_id=self.buyer_id, fingerprint=self.fingerprint, transaction_id=self.transaction_id, id=self.id)
__all__ = ['payment_flows_private_payment_methods_alipay_details']