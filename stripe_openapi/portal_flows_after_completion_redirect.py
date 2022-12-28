from sqlalchemy import Column, Integer, String

class Portal_Flows_After_Completion_Redirect(Base):
    __tablename__ = 'portal_flows_after_completion_redirect'
    return_url = Column(String, comment='The URL the customer will be redirected to after the flow is completed')
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Portal_Flows_After_Completion_Redirect(return_url={return_url!r}, id={id!r})'.format(return_url=self.return_url, id=self.id)
__all__ = ['portal_flows_after_completion_redirect']