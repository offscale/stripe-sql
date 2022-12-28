from sqlalchemy import Column, Integer

class Balance_Amount_By_Source_Type(Base):
    __tablename__ = 'balance_amount_by_source_type'
    bank_account = Column(Integer, comment='Amount for bank account', nullable=True)
    card = Column(Integer, comment='Amount for card', nullable=True)
    fpx = Column(Integer, comment='Amount for FPX', nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Balance_Amount_By_Source_Type(bank_account={bank_account!r}, card={card!r}, fpx={fpx!r}, id={id!r})'.format(bank_account=self.bank_account, card=self.card, fpx=self.fpx, id=self.id)
__all__ = ['balance_amount_by_source_type']