from sqlalchemy import Boolean, Column, Integer

class Payment_Intent_Processing_Customer_Notification(Base):
    __tablename__ = 'payment_intent_processing_customer_notification'
    approval_requested = Column(Boolean, comment='Whether customer approval has been requested for this payment. For payments greater than INR 15000 or mandate amount, the customer must provide explicit approval of the payment with their bank', nullable=True)
    completes_at = Column(Integer, comment='If customer approval is required, they need to provide approval before this time', nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Payment_Intent_Processing_Customer_Notification(approval_requested={approval_requested!r}, completes_at={completes_at!r}, id={id!r})'.format(approval_requested=self.approval_requested, completes_at=self.completes_at, id=self.id)
__all__ = ['payment_intent_processing_customer_notification']