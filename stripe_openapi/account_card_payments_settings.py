from sqlalchemy import Column, Integer, String

class Account_Card_Payments_Settings(Base):
    __tablename__ = 'account_card_payments_settings'
    decline_on = Column(AccountDeclineChargeOn, nullable=True)
    statement_descriptor_prefix = Column(String, comment='The default text that appears on credit card statements when a charge is made. This field prefixes any dynamic `statement_descriptor` specified on the charge. `statement_descriptor_prefix` is useful for maximizing descriptor space for the dynamic portion', nullable=True)
    statement_descriptor_prefix_kana = Column(String, comment='The Kana variation of the default text that appears on credit card statements when a charge is made (Japan only). This field prefixes any dynamic `statement_descriptor_suffix_kana` specified on the charge. `statement_descriptor_prefix_kana` is useful for maximizing descriptor space for the dynamic portion', nullable=True)
    statement_descriptor_prefix_kanji = Column(String, comment='The Kanji variation of the default text that appears on credit card statements when a charge is made (Japan only). This field prefixes any dynamic `statement_descriptor_suffix_kanji` specified on the charge. `statement_descriptor_prefix_kanji` is useful for maximizing descriptor space for the dynamic portion', nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Account_Card_Payments_Settings(decline_on={decline_on!r}, statement_descriptor_prefix={statement_descriptor_prefix!r}, statement_descriptor_prefix_kana={statement_descriptor_prefix_kana!r}, statement_descriptor_prefix_kanji={statement_descriptor_prefix_kanji!r}, id={id!r})'.format(decline_on=self.decline_on, statement_descriptor_prefix=self.statement_descriptor_prefix, statement_descriptor_prefix_kana=self.statement_descriptor_prefix_kana, statement_descriptor_prefix_kanji=self.statement_descriptor_prefix_kanji, id=self.id)
__all__ = ['account_card_payments_settings']