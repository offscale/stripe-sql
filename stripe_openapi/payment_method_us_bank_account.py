from sqlalchemy import Column, String

class Payment_Method_Us_Bank_Account(Base):
    __tablename__ = 'payment_method_us_bank_account'
    account_holder_type = Column(String, comment='Account holder type: individual or company', nullable=True)
    account_type = Column(String, comment='Account type: checkings or savings. Defaults to checking if omitted', nullable=True)
    bank_name = Column(String, comment='The name of the bank', nullable=True, primary_key=True)
    financial_connections_account = Column(String, comment='The ID of the Financial Connections Account used to create the payment method', nullable=True)
    fingerprint = Column(String, comment='Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same', nullable=True)
    last4 = Column(String, comment='Last four digits of the bank account number', nullable=True)
    networks = Column(UsBankAccountNetworks, comment='Contains information about US bank account networks that can be used', nullable=True)
    routing_number = Column(String, comment='Routing number of the bank account', nullable=True)

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Payment_Method_Us_Bank_Account(account_holder_type={account_holder_type!r}, account_type={account_type!r}, bank_name={bank_name!r}, financial_connections_account={financial_connections_account!r}, fingerprint={fingerprint!r}, last4={last4!r}, networks={networks!r}, routing_number={routing_number!r})'.format(account_holder_type=self.account_holder_type, account_type=self.account_type, bank_name=self.bank_name, financial_connections_account=self.financial_connections_account, fingerprint=self.fingerprint, last4=self.last4, networks=self.networks, routing_number=self.routing_number)
__all__ = ['payment_method_us_bank_account']