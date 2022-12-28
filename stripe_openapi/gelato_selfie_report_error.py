from sqlalchemy import Column, Integer, String

class Gelato_Selfie_Report_Error(Base):
    __tablename__ = 'gelato_selfie_report_error'
    code = Column(String, comment='A short machine-readable string giving the reason for the verification failure', nullable=True)
    reason = Column(String, comment='A human-readable message giving the reason for the failure. These messages can be shown to your users', nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Gelato_Selfie_Report_Error(code={code!r}, reason={reason!r}, id={id!r})'.format(code=self.code, reason=self.reason, id=self.id)
__all__ = ['gelato_selfie_report_error']