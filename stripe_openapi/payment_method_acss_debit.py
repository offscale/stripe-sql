from sqlalchemy import Column, String

class Payment_Method_Acss_Debit(Base):
    __tablename__ = 'payment_method_acss_debit'
    bank_name = Column(String, comment='Name of the bank associated with the bank account', nullable=True, primary_key=True)
    fingerprint = Column(String, comment='Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same', nullable=True)
    institution_number = Column(String, comment='Institution number of the bank account', nullable=True)
    last4 = Column(String, comment='Last four digits of the bank account number', nullable=True)
    transit_number = Column(String, comment='Transit number of the bank account', nullable=True)

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Payment_Method_Acss_Debit(bank_name={bank_name!r}, fingerprint={fingerprint!r}, institution_number={institution_number!r}, last4={last4!r}, transit_number={transit_number!r})'.format(bank_name=self.bank_name, fingerprint=self.fingerprint, institution_number=self.institution_number, last4=self.last4, transit_number=self.transit_number)
__all__ = ['payment_method_acss_debit']