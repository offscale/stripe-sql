from sqlalchemy import Column, Integer, String

class Payment_Method_Details_Oxxo(Base):
    __tablename__ = 'payment_method_details_oxxo'
    number = Column(String, comment='OXXO reference number', nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Payment_Method_Details_Oxxo(number={number!r}, id={id!r})'.format(number=self.number, id=self.id)
__all__ = ['payment_method_details_oxxo']