from sqlalchemy import Column, String

class Tax_Id_Verification(Base):
    __tablename__ = 'tax_id_verification'
    status = Column(String, comment='Verification status, one of `pending`, `verified`, `unverified`, or `unavailable`')
    verified_address = Column(String, comment='Verified address', nullable=True)
    verified_name = Column(String, comment='Verified name', nullable=True, primary_key=True)

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Tax_Id_Verification(status={status!r}, verified_address={verified_address!r}, verified_name={verified_name!r})'.format(status=self.status, verified_address=self.verified_address, verified_name=self.verified_name)
__all__ = ['tax_id_verification']