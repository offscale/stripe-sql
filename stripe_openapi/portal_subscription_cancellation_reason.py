from sqlalchemy import Boolean, Column, Integer

class Portal_Subscription_Cancellation_Reason(Base):
    __tablename__ = 'portal_subscription_cancellation_reason'
    enabled = Column(Boolean, comment='Whether the feature is enabled')
    options = Column(ARRAY(String), comment='Which cancellation reasons will be given as options to the customer')
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Portal_Subscription_Cancellation_Reason(enabled={enabled!r}, options={options!r}, id={id!r})'.format(enabled=self.enabled, options=self.options, id=self.id)
__all__ = ['portal_subscription_cancellation_reason']