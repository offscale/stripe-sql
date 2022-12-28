from sqlalchemy import Column, Integer

class Payment_Method_Afterpay_Clearpay(Base):
    __tablename__ = 'payment_method_afterpay_clearpay'
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Payment_Method_Afterpay_Clearpay(id={id!r})'.format(id=self.id)
__all__ = ['payment_method_afterpay_clearpay']