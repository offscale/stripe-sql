from sqlalchemy import Column, Integer

class Bank_Connections_Resource_Balance_Api_Resource_Cash_Balance(Base):
    __tablename__ = 'bank_connections_resource_balance_api_resource_cash_balance'
    available = Column(JSON, comment='The funds available to the account holder. Typically this is the current balance less any holds.\n\nEach key is a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase.\n\nEach value is a integer amount. A positive amount indicates money owed to the account holder. A negative amount indicates money owed by the account holder', nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Bank_Connections_Resource_Balance_Api_Resource_Cash_Balance(available={available!r}, id={id!r})'.format(available=self.available, id=self.id)
__all__ = ['bank_connections_resource_balance_api_resource_cash_balance']