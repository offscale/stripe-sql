from sqlalchemy import Column, Integer, String

class Setup_Intent_Payment_Method_Options_Acss_Debit(Base):
    __tablename__ = 'setup_intent_payment_method_options_acss_debit'
    currency = Column(String, comment='Currency supported by the bank account', nullable=True)
    mandate_options = Column(SetupIntentPaymentMethodOptionsMandateOptionsAcssDebit, nullable=True)
    verification_method = Column(String, comment='Bank account verification method', nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Setup_Intent_Payment_Method_Options_Acss_Debit(currency={currency!r}, mandate_options={mandate_options!r}, verification_method={verification_method!r}, id={id!r})'.format(currency=self.currency, mandate_options=self.mandate_options, verification_method=self.verification_method, id=self.id)
__all__ = ['setup_intent_payment_method_options_acss_debit']