from sqlalchemy import Column, String

class Funding_Instructions_Bank_Transfer_Sort_Code_Record(Base):
    """
    Sort Code Records contain U.K. bank account details per the sort code format.
        """
    __tablename__ = 'funding_instructions_bank_transfer_sort_code_record'
    account_holder_name = Column(String, comment='The name of the person or business that owns the bank account', primary_key=True)
    account_number = Column(String, comment='The account number')
    sort_code = Column(String, comment='The six-digit sort code')

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Funding_Instructions_Bank_Transfer_Sort_Code_Record(account_holder_name={account_holder_name!r}, account_number={account_number!r}, sort_code={sort_code!r})'.format(account_holder_name=self.account_holder_name, account_number=self.account_number, sort_code=self.sort_code)
__all__ = ['funding_instructions_bank_transfer_sort_code_record']