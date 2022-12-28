from sqlalchemy import Column, Integer, String

class Portal_Flows_Flow(Base):
    __tablename__ = 'portal_flows_flow'
    after_completion = Column(PortalFlowsFlowAfterCompletion)
    subscription_cancel = Column(PortalFlowsFlowSubscriptionCancel, comment='Configuration when `flow.type=subscription_cancel`', nullable=True)
    type = Column(String, comment='Type of flow that the customer will go through')
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Portal_Flows_Flow(after_completion={after_completion!r}, subscription_cancel={subscription_cancel!r}, type={type!r}, id={id!r})'.format(after_completion=self.after_completion, subscription_cancel=self.subscription_cancel, type=self.type, id=self.id)
__all__ = ['portal_flows_flow']