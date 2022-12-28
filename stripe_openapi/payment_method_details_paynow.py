from sqlalchemy import Column, Integer, String

class Payment_Method_Details_Paynow(Base):
    __tablename__ = 'payment_method_details_paynow'
    reference = Column(String, comment='Reference number associated with this PayNow payment', nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Payment_Method_Details_Paynow(reference={reference!r}, id={id!r})'.format(reference=self.reference, id=self.id)
__all__ = ['payment_method_details_paynow']