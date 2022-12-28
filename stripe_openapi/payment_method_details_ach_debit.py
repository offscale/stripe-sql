from sqlalchemy import Column, String

class Payment_Method_Details_Ach_Debit(Base):
    __tablename__ = 'payment_method_details_ach_debit'
    account_holder_type = Column(String, comment='Type of entity that holds the account. This can be either `individual` or `company`', nullable=True)
    bank_name = Column(String, comment='Name of the bank associated with the bank account', nullable=True, primary_key=True)
    country = Column(String, comment='Two-letter ISO code representing the country the bank account is located in', nullable=True)
    fingerprint = Column(String, comment='Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same', nullable=True)
    last4 = Column(String, comment='Last four digits of the bank account number', nullable=True)
    routing_number = Column(String, comment='Routing transit number of the bank account', nullable=True)

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Payment_Method_Details_Ach_Debit(account_holder_type={account_holder_type!r}, bank_name={bank_name!r}, country={country!r}, fingerprint={fingerprint!r}, last4={last4!r}, routing_number={routing_number!r})'.format(account_holder_type=self.account_holder_type, bank_name=self.bank_name, country=self.country, fingerprint=self.fingerprint, last4=self.last4, routing_number=self.routing_number)
__all__ = ['payment_method_details_ach_debit']