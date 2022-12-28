from sqlalchemy import Column, String

class Payment_Method_Details_Wechat_Pay(Base):
    __tablename__ = 'payment_method_details_wechat_pay'
    fingerprint = Column(String, comment='Uniquely identifies this particular WeChat Pay account. You can use this attribute to check whether two WeChat accounts are the same', nullable=True)
    transaction_id = Column(String, comment='Transaction ID of this particular WeChat Pay transaction', nullable=True, primary_key=True)

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Payment_Method_Details_Wechat_Pay(fingerprint={fingerprint!r}, transaction_id={transaction_id!r})'.format(fingerprint=self.fingerprint, transaction_id=self.transaction_id)
__all__ = ['payment_method_details_wechat_pay']