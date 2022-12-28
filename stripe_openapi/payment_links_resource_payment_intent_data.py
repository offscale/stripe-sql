from sqlalchemy import Column, Integer, String

class Payment_Links_Resource_Payment_Intent_Data(Base):
    __tablename__ = 'payment_links_resource_payment_intent_data'
    capture_method = Column(String, comment="Indicates when the funds will be captured from the customer's account", nullable=True)
    setup_future_usage = Column(String, comment='Indicates that you intend to make future payments with the payment method collected during checkout', nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Payment_Links_Resource_Payment_Intent_Data(capture_method={capture_method!r}, setup_future_usage={setup_future_usage!r}, id={id!r})'.format(capture_method=self.capture_method, setup_future_usage=self.setup_future_usage, id=self.id)
__all__ = ['payment_links_resource_payment_intent_data']