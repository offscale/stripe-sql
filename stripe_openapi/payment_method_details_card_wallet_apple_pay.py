from sqlalchemy import Column, Integer

class Payment_Method_Details_Card_Wallet_Apple_Pay(Base):
    __tablename__ = 'payment_method_details_card_wallet_apple_pay'
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Payment_Method_Details_Card_Wallet_Apple_Pay(id={id!r})'.format(id=self.id)
__all__ = ['payment_method_details_card_wallet_apple_pay']