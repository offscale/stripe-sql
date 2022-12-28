from sqlalchemy import Column, String

class Received_Payment_Method_Details_Financial_Account(Base):
    __tablename__ = 'received_payment_method_details_financial_account'
    id = Column(String, comment='The FinancialAccount ID', primary_key=True)
    network = Column(String, comment='The rails the ReceivedCredit was sent over. A FinancialAccount can only send funds over `stripe`')

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Received_Payment_Method_Details_Financial_Account(id={id!r}, network={network!r})'.format(id=self.id, network=self.network)
__all__ = ['received_payment_method_details_financial_account']