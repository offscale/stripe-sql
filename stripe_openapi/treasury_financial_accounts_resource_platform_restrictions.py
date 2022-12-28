from sqlalchemy import Column, Integer, String

class Treasury_Financial_Accounts_Resource_Platform_Restrictions(Base):
    """
    Restrictions that a Connect Platform has placed on this FinancialAccount.
        """
    __tablename__ = 'treasury_financial_accounts_resource_platform_restrictions'
    inbound_flows = Column(String, comment='Restricts all inbound money movement', nullable=True)
    outbound_flows = Column(String, comment='Restricts all outbound money movement', nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Treasury_Financial_Accounts_Resource_Platform_Restrictions(inbound_flows={inbound_flows!r}, outbound_flows={outbound_flows!r}, id={id!r})'.format(inbound_flows=self.inbound_flows, outbound_flows=self.outbound_flows, id=self.id)
__all__ = ['treasury_financial_accounts_resource_platform_restrictions']