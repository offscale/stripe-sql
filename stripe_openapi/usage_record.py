from sqlalchemy import Boolean, Column, Integer, String

class Usage_Record(Base):
    """
        Usage records allow you to report customer usage and metrics to Stripe for
    
        metered billing of subscription prices.
    
        Related guide: [Metered Billing](https://stripe.com/docs/billing/subscriptions/metered-billing).
    
        """
    __tablename__ = 'usage_record'
    id = Column(String, comment='Unique identifier for the object', primary_key=True)
    livemode = Column(Boolean, comment='Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode')
    object = Column(String, comment="String representing the object's type. Objects of the same type share the same value")
    quantity = Column(Integer, comment='The usage quantity for the specified date')
    subscription_item = Column(String, comment='The ID of the subscription item this usage record contains data for')
    timestamp = Column(Integer, comment='The timestamp when this usage occurred')

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Usage_Record(id={id!r}, livemode={livemode!r}, object={object!r}, quantity={quantity!r}, subscription_item={subscription_item!r}, timestamp={timestamp!r})'.format(id=self.id, livemode=self.livemode, object=self.object, quantity=self.quantity, subscription_item=self.subscription_item, timestamp=self.timestamp)
__all__ = ['usage_record']