from sqlalchemy import Column, Integer

class Account_Card_Issuing_Settings(Base):
    __tablename__ = 'account_card_issuing_settings'
    tos_acceptance = Column(CardIssuingAccountTermsOfService, nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Account_Card_Issuing_Settings(tos_acceptance={tos_acceptance!r}, id={id!r})'.format(tos_acceptance=self.tos_acceptance, id=self.id)
__all__ = ['account_card_issuing_settings']