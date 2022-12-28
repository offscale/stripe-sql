from sqlalchemy import Column, Integer, String

class Mandate_Payment_Method_Details(Base):
    __tablename__ = 'mandate_payment_method_details'
    acss_debit = Column(MandateAcssDebit, nullable=True)
    au_becs_debit = Column(MandateAuBecsDebit, nullable=True)
    bacs_debit = Column(MandateBacsDebit, nullable=True)
    blik = Column(MandateBlik, nullable=True)
    card = Column(CardMandatePaymentMethodDetails, nullable=True)
    link = Column(MandateLink, nullable=True)
    sepa_debit = Column(MandateSepaDebit, nullable=True)
    type = Column(String, comment='The type of the payment method associated with this mandate. An additional hash is included on `payment_method_details` with a name matching this value. It contains mandate information specific to the payment method')
    us_bank_account = Column(MandateUsBankAccount, nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Mandate_Payment_Method_Details(acss_debit={acss_debit!r}, au_becs_debit={au_becs_debit!r}, bacs_debit={bacs_debit!r}, blik={blik!r}, card={card!r}, link={link!r}, sepa_debit={sepa_debit!r}, type={type!r}, us_bank_account={us_bank_account!r}, id={id!r})'.format(acss_debit=self.acss_debit, au_becs_debit=self.au_becs_debit, bacs_debit=self.bacs_debit, blik=self.blik, card=self.card, link=self.link, sepa_debit=self.sepa_debit, type=self.type, us_bank_account=self.us_bank_account, id=self.id)
__all__ = ['mandate_payment_method_details']