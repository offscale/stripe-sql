from sqlalchemy import Column, Integer, String

class Treasury_Inbound_Transfers_Resource_Failure_Details(Base):
    __tablename__ = 'treasury_inbound_transfers_resource_failure_details'
    code = Column(String, comment='Reason for the failure')
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Treasury_Inbound_Transfers_Resource_Failure_Details(code={code!r}, id={id!r})'.format(code=self.code, id=self.id)
__all__ = ['treasury_inbound_transfers_resource_failure_details']