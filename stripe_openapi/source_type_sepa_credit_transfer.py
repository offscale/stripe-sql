from sqlalchemy import Column, Integer, String

class Source_Type_Sepa_Credit_Transfer(Base):
    __tablename__ = 'source_type_sepa_credit_transfer'
    bank_name = Column(String, nullable=True)
    bic = Column(String, nullable=True)
    iban = Column(String, nullable=True)
    refund_account_holder_address_city = Column(String, nullable=True)
    refund_account_holder_address_country = Column(String, nullable=True)
    refund_account_holder_address_line1 = Column(String, nullable=True)
    refund_account_holder_address_line2 = Column(String, nullable=True)
    refund_account_holder_address_postal_code = Column(String, nullable=True)
    refund_account_holder_address_state = Column(String, nullable=True)
    refund_account_holder_name = Column(String, nullable=True)
    refund_iban = Column(String, nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Source_Type_Sepa_Credit_Transfer(bank_name={bank_name!r}, bic={bic!r}, iban={iban!r}, refund_account_holder_address_city={refund_account_holder_address_city!r}, refund_account_holder_address_country={refund_account_holder_address_country!r}, refund_account_holder_address_line1={refund_account_holder_address_line1!r}, refund_account_holder_address_line2={refund_account_holder_address_line2!r}, refund_account_holder_address_postal_code={refund_account_holder_address_postal_code!r}, refund_account_holder_address_state={refund_account_holder_address_state!r}, refund_account_holder_name={refund_account_holder_name!r}, refund_iban={refund_iban!r}, id={id!r})'.format(bank_name=self.bank_name, bic=self.bic, iban=self.iban, refund_account_holder_address_city=self.refund_account_holder_address_city, refund_account_holder_address_country=self.refund_account_holder_address_country, refund_account_holder_address_line1=self.refund_account_holder_address_line1, refund_account_holder_address_line2=self.refund_account_holder_address_line2, refund_account_holder_address_postal_code=self.refund_account_holder_address_postal_code, refund_account_holder_address_state=self.refund_account_holder_address_state, refund_account_holder_name=self.refund_account_holder_name, refund_iban=self.refund_iban, id=self.id)
__all__ = ['source_type_sepa_credit_transfer']