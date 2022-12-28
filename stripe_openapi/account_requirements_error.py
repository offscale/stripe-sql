from sqlalchemy import Column, Integer, String

class Account_Requirements_Error(Base):
    __tablename__ = 'account_requirements_error'
    code = Column(String, comment='The code for the type of error')
    reason = Column(String, comment='An informative message that indicates the error type and provides additional details about the error')
    requirement = Column(String, comment='The specific user onboarding requirement field (in the requirements hash) that needs to be resolved')
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Account_Requirements_Error(code={code!r}, reason={reason!r}, requirement={requirement!r}, id={id!r})'.format(code=self.code, reason=self.reason, requirement=self.requirement, id=self.id)
__all__ = ['account_requirements_error']