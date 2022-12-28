from sqlalchemy import Column, Integer

class Treasury_Financial_Accounts_Resource_Balance(Base):
    """
    Balance information for the FinancialAccount
        """
    __tablename__ = 'treasury_financial_accounts_resource_balance'
    cash = Column(JSON, comment='Funds the user can spend right now')
    inbound_pending = Column(JSON, comment='Funds not spendable yet, but will become available at a later time')
    outbound_pending = Column(JSON, comment='Funds in the account, but not spendable because they are being held for pending outbound flows')
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Treasury_Financial_Accounts_Resource_Balance(cash={cash!r}, inbound_pending={inbound_pending!r}, outbound_pending={outbound_pending!r}, id={id!r})'.format(cash=self.cash, inbound_pending=self.inbound_pending, outbound_pending=self.outbound_pending, id=self.id)
__all__ = ['treasury_financial_accounts_resource_balance']