from sqlalchemy import Column, Integer, String

class Bank_Connections_Resource_Accountholder(Base):
    __tablename__ = 'bank_connections_resource_accountholder'
    account = Column(Account, comment='The ID of the Stripe account this account belongs to. Should only be present if `account_holder.type` is `account`', nullable=True)
    customer = Column(Customer, comment='ID of the Stripe customer this account belongs to. Present if and only if `account_holder.type` is `customer`', nullable=True)
    type = Column(String, comment='Type of account holder that this account belongs to')
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Bank_Connections_Resource_Accountholder(account={account!r}, customer={customer!r}, type={type!r}, id={id!r})'.format(account=self.account, customer=self.customer, type=self.type, id=self.id)
__all__ = ['bank_connections_resource_accountholder']