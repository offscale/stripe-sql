from sqlalchemy import Column, Integer, String

class Payment_Method_Details_Bancontact(Base):
    __tablename__ = 'payment_method_details_bancontact'
    bank_code = Column(String, comment='Bank code of bank associated with the bank account', nullable=True)
    bank_name = Column(String, comment='Name of the bank associated with the bank account', nullable=True)
    bic = Column(String, comment='Bank Identifier Code of the bank associated with the bank account', nullable=True)
    generated_sepa_debit = Column(PaymentMethod, comment='The ID of the SEPA Direct Debit PaymentMethod which was generated by this Charge', nullable=True)
    generated_sepa_debit_mandate = Column(Mandate, comment='The mandate for the SEPA Direct Debit PaymentMethod which was generated by this Charge', nullable=True)
    iban_last4 = Column(String, comment='Last four characters of the IBAN', nullable=True)
    preferred_language = Column(String, comment='Preferred language of the Bancontact authorization page that the customer is redirected to.\nCan be one of `en`, `de`, `fr`, or `nl`', nullable=True)
    verified_name = Column(String, comment="Owner's verified full name. Values are verified or provided by Bancontact directly\n(if supported) at the time of authorization or settlement. They cannot be set or mutated", nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Payment_Method_Details_Bancontact(bank_code={bank_code!r}, bank_name={bank_name!r}, bic={bic!r}, generated_sepa_debit={generated_sepa_debit!r}, generated_sepa_debit_mandate={generated_sepa_debit_mandate!r}, iban_last4={iban_last4!r}, preferred_language={preferred_language!r}, verified_name={verified_name!r}, id={id!r})'.format(bank_code=self.bank_code, bank_name=self.bank_name, bic=self.bic, generated_sepa_debit=self.generated_sepa_debit, generated_sepa_debit_mandate=self.generated_sepa_debit_mandate, iban_last4=self.iban_last4, preferred_language=self.preferred_language, verified_name=self.verified_name, id=self.id)
__all__ = ['payment_method_details_bancontact']