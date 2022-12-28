from sqlalchemy import Column, Integer, String

class Payment_Method_Details_Sepa_Debit(Base):
    __tablename__ = 'payment_method_details_sepa_debit'
    bank_code = Column(String, comment='Bank code of bank associated with the bank account', nullable=True)
    branch_code = Column(String, comment='Branch code of bank associated with the bank account', nullable=True)
    country = Column(String, comment='Two-letter ISO code representing the country the bank account is located in', nullable=True)
    fingerprint = Column(String, comment='Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same', nullable=True)
    last4 = Column(String, comment='Last four characters of the IBAN', nullable=True)
    mandate = Column(String, comment='ID of the mandate used to make this payment', nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Payment_Method_Details_Sepa_Debit(bank_code={bank_code!r}, branch_code={branch_code!r}, country={country!r}, fingerprint={fingerprint!r}, last4={last4!r}, mandate={mandate!r}, id={id!r})'.format(bank_code=self.bank_code, branch_code=self.branch_code, country=self.country, fingerprint=self.fingerprint, last4=self.last4, mandate=self.mandate, id=self.id)
__all__ = ['payment_method_details_sepa_debit']