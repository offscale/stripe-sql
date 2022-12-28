from sqlalchemy import Column, Integer, String

class Secret_Service_Resource_Scope(Base):
    __tablename__ = 'secret_service_resource_scope'
    type = Column(String, comment='The secret scope type')
    user = Column(String, comment='The user ID, if type is set to "user"', nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Secret_Service_Resource_Scope(type={type!r}, user={user!r}, id={id!r})'.format(type=self.type, user=self.user, id=self.id)
__all__ = ['secret_service_resource_scope']