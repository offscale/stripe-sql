from sqlalchemy import Column, Integer

class Payment_Flows_Private_Payment_Methods_Alipay(Base):
    __tablename__ = 'payment_flows_private_payment_methods_alipay'
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Payment_Flows_Private_Payment_Methods_Alipay(id={id!r})'.format(id=self.id)
__all__ = ['payment_flows_private_payment_methods_alipay']