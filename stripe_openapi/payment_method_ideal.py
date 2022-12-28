from sqlalchemy import Column, Integer, String

class Payment_Method_Ideal(Base):
    __tablename__ = 'payment_method_ideal'
    bank = Column(String, comment="The customer's bank, if provided. Can be one of `abn_amro`, `asn_bank`, `bunq`, `handelsbanken`, `ing`, `knab`, `moneyou`, `rabobank`, `regiobank`, `revolut`, `sns_bank`, `triodos_bank`, or `van_lanschot`", nullable=True)
    bic = Column(String, comment="The Bank Identifier Code of the customer's bank, if the bank was provided", nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Payment_Method_Ideal(bank={bank!r}, bic={bic!r}, id={id!r})'.format(bank=self.bank, bic=self.bic, id=self.id)
__all__ = ['payment_method_ideal']