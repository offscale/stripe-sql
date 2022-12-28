from sqlalchemy import Column, Integer

class Setup_Intent_Payment_Method_Options_Mandate_Options_Sepa_Debit(Base):
    __tablename__ = 'setup_intent_payment_method_options_mandate_options_sepa_debit'
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Setup_Intent_Payment_Method_Options_Mandate_Options_Sepa_Debit(id={id!r})'.format(id=self.id)
__all__ = ['setup_intent_payment_method_options_mandate_options_sepa_debit']