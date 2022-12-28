from sqlalchemy import Column, Integer, String

class Source_Type_Sepa_Debit(Base):
    __tablename__ = 'source_type_sepa_debit'
    bank_code = Column(String, nullable=True)
    branch_code = Column(String, nullable=True)
    country = Column(String, nullable=True)
    fingerprint = Column(String, nullable=True)
    last4 = Column(String, nullable=True)
    mandate_reference = Column(String, nullable=True)
    mandate_url = Column(String, nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Source_Type_Sepa_Debit(bank_code={bank_code!r}, branch_code={branch_code!r}, country={country!r}, fingerprint={fingerprint!r}, last4={last4!r}, mandate_reference={mandate_reference!r}, mandate_url={mandate_url!r}, id={id!r})'.format(bank_code=self.bank_code, branch_code=self.branch_code, country=self.country, fingerprint=self.fingerprint, last4=self.last4, mandate_reference=self.mandate_reference, mandate_url=self.mandate_url, id=self.id)
__all__ = ['source_type_sepa_debit']