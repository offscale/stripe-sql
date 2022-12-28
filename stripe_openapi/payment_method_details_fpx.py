from sqlalchemy import Column, String

class Payment_Method_Details_Fpx(Base):
    __tablename__ = 'payment_method_details_fpx'
    account_holder_type = Column(String, comment='Account holder type, if provided. Can be one of `individual` or `company`', nullable=True)
    bank = Column(String, comment="The customer's bank. Can be one of `affin_bank`, `agrobank`, `alliance_bank`, `ambank`, `bank_islam`, `bank_muamalat`, `bank_rakyat`, `bsn`, `cimb`, `hong_leong_bank`, `hsbc`, `kfh`, `maybank2u`, `ocbc`, `public_bank`, `rhb`, `standard_chartered`, `uob`, `deutsche_bank`, `maybank2e`, `pb_enterprise`, or `bank_of_china`")
    transaction_id = Column(String, comment='Unique transaction id generated by FPX for every request from the merchant', nullable=True, primary_key=True)

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Payment_Method_Details_Fpx(account_holder_type={account_holder_type!r}, bank={bank!r}, transaction_id={transaction_id!r})'.format(account_holder_type=self.account_holder_type, bank=self.bank, transaction_id=self.transaction_id)
__all__ = ['payment_method_details_fpx']