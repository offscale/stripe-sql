from sqlalchemy import Column, Integer

class Card_Mandate_Payment_Method_Details(Base):
    __tablename__ = 'card_mandate_payment_method_details'
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Card_Mandate_Payment_Method_Details(id={id!r})'.format(id=self.id)
__all__ = ['card_mandate_payment_method_details']