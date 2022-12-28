from sqlalchemy import Column, Integer, String

class Portal_Flows_Flow_Subscription_Cancel(Base):
    __tablename__ = 'portal_flows_flow_subscription_cancel'
    subscription = Column(String, comment='The ID of the subscription to be canceled')
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Portal_Flows_Flow_Subscription_Cancel(subscription={subscription!r}, id={id!r})'.format(subscription=self.subscription, id=self.id)
__all__ = ['portal_flows_flow_subscription_cancel']