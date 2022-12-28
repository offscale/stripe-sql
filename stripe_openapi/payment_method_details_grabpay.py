from sqlalchemy import Column, String

class Payment_Method_Details_Grabpay(Base):
    __tablename__ = 'payment_method_details_grabpay'
    transaction_id = Column(String, comment='Unique transaction id generated by GrabPay', nullable=True, primary_key=True)

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Payment_Method_Details_Grabpay(transaction_id={transaction_id!r})'.format(transaction_id=self.transaction_id)
__all__ = ['payment_method_details_grabpay']