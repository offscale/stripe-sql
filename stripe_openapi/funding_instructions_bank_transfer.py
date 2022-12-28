from sqlalchemy import Column, Integer, String

class Funding_Instructions_Bank_Transfer(Base):
    __tablename__ = 'funding_instructions_bank_transfer'
    country = Column(String, comment='The country of the bank account to fund')
    financial_addresses = Column(list, comment='A list of financial addresses that can be used to fund a particular balance')
    type = Column(String, comment='The bank_transfer type')
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Funding_Instructions_Bank_Transfer(country={country!r}, financial_addresses={financial_addresses!r}, type={type!r}, id={id!r})'.format(country=self.country, financial_addresses=self.financial_addresses, type=self.type, id=self.id)
__all__ = ['funding_instructions_bank_transfer']