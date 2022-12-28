from sqlalchemy import Column, Integer, String

class Payment_Intent_Next_Action_Konbini_Ministop(Base):
    __tablename__ = 'payment_intent_next_action_konbini_ministop'
    confirmation_number = Column(String, comment='The confirmation number', nullable=True)
    payment_code = Column(String, comment='The payment code')
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Payment_Intent_Next_Action_Konbini_Ministop(confirmation_number={confirmation_number!r}, payment_code={payment_code!r}, id={id!r})'.format(confirmation_number=self.confirmation_number, payment_code=self.payment_code, id=self.id)
__all__ = ['payment_intent_next_action_konbini_ministop']