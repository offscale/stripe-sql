from sqlalchemy import Column, String

class Account_Sepa_Debit_Payments_Settings(Base):
    __tablename__ = 'account_sepa_debit_payments_settings'
    creditor_id = Column(String, comment='SEPA creditor identifier that identifies the company making the payment', nullable=True, primary_key=True)

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Account_Sepa_Debit_Payments_Settings(creditor_id={creditor_id!r})'.format(creditor_id=self.creditor_id)
__all__ = ['account_sepa_debit_payments_settings']