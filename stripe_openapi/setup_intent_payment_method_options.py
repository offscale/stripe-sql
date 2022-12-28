from sqlalchemy import Column, Integer

class Setup_Intent_Payment_Method_Options(Base):
    __tablename__ = 'setup_intent_payment_method_options'
    acss_debit = Column(SetupIntentPaymentMethodOptionsAcssDebit, nullable=True)
    blik = Column(SetupIntentPaymentMethodOptionsBlik, nullable=True)
    card = Column(SetupIntentPaymentMethodOptionsCard, nullable=True)
    link = Column(SetupIntentPaymentMethodOptionsLink, nullable=True)
    sepa_debit = Column(SetupIntentPaymentMethodOptionsSepaDebit, nullable=True)
    us_bank_account = Column(SetupIntentPaymentMethodOptionsUsBankAccount, nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Setup_Intent_Payment_Method_Options(acss_debit={acss_debit!r}, blik={blik!r}, card={card!r}, link={link!r}, sepa_debit={sepa_debit!r}, us_bank_account={us_bank_account!r}, id={id!r})'.format(acss_debit=self.acss_debit, blik=self.blik, card=self.card, link=self.link, sepa_debit=self.sepa_debit, us_bank_account=self.us_bank_account, id=self.id)
__all__ = ['setup_intent_payment_method_options']