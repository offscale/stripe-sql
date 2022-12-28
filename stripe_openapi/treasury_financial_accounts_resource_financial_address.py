from sqlalchemy import Column, Integer, String

class Treasury_Financial_Accounts_Resource_Financial_Address(Base):
    """
    FinancialAddresses contain identifying information that resolves to a FinancialAccount.
        """
    __tablename__ = 'treasury_financial_accounts_resource_financial_address'
    aba = Column(TreasuryFinancialAccountsResourceAbaRecord, nullable=True)
    supported_networks = Column(ARRAY(String), comment='The list of networks that the address supports', nullable=True)
    type = Column(String, comment='The type of financial address')
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Treasury_Financial_Accounts_Resource_Financial_Address(aba={aba!r}, supported_networks={supported_networks!r}, type={type!r}, id={id!r})'.format(aba=self.aba, supported_networks=self.supported_networks, type=self.type, id=self.id)
__all__ = ['treasury_financial_accounts_resource_financial_address']