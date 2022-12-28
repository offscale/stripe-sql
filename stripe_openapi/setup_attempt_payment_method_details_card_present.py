from sqlalchemy import Column, Integer

class Setup_Attempt_Payment_Method_Details_Card_Present(Base):
    __tablename__ = 'setup_attempt_payment_method_details_card_present'
    generated_card = Column(PaymentMethod, comment='The ID of the Card PaymentMethod which was generated by this SetupAttempt', nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Setup_Attempt_Payment_Method_Details_Card_Present(generated_card={generated_card!r}, id={id!r})'.format(generated_card=self.generated_card, id=self.id)
__all__ = ['setup_attempt_payment_method_details_card_present']