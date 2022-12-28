from sqlalchemy import Column, Integer

class Treasury_Financial_Accounts_Resource_Outbound_Payments(Base):
    """
    Settings related to Outbound Payments features on a Financial Account
        """
    __tablename__ = 'treasury_financial_accounts_resource_outbound_payments'
    ach = Column(TreasuryFinancialAccountsResourceAchToggleSettings, nullable=True)
    us_domestic_wire = Column(TreasuryFinancialAccountsResourceToggleSettings, nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Treasury_Financial_Accounts_Resource_Outbound_Payments(ach={ach!r}, us_domestic_wire={us_domestic_wire!r}, id={id!r})'.format(ach=self.ach, us_domestic_wire=self.us_domestic_wire, id=self.id)
__all__ = ['treasury_financial_accounts_resource_outbound_payments']