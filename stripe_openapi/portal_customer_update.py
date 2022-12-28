from sqlalchemy import Boolean, Column, Integer

class Portal_Customer_Update(Base):
    __tablename__ = 'portal_customer_update'
    allowed_updates = Column(ARRAY(String), comment='The types of customer updates that are supported. When empty, customers are not updateable')
    enabled = Column(Boolean, comment='Whether the feature is enabled')
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Portal_Customer_Update(allowed_updates={allowed_updates!r}, enabled={enabled!r}, id={id!r})'.format(allowed_updates=self.allowed_updates, enabled=self.enabled, id=self.id)
__all__ = ['portal_customer_update']