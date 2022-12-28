from sqlalchemy import Column, Integer

class Setup_Attempt_Payment_Method_Details_Acss_Debit(Base):
    __tablename__ = 'setup_attempt_payment_method_details_acss_debit'
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Setup_Attempt_Payment_Method_Details_Acss_Debit(id={id!r})'.format(id=self.id)
__all__ = ['setup_attempt_payment_method_details_acss_debit']