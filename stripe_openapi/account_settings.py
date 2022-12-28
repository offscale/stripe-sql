from sqlalchemy import Column, Integer

class Account_Settings(Base):
    __tablename__ = 'account_settings'
    bacs_debit_payments = Column(AccountBacsDebitPaymentsSettings, nullable=True)
    branding = Column(AccountBrandingSettings)
    card_issuing = Column(AccountCardIssuingSettings, nullable=True)
    card_payments = Column(AccountCardPaymentsSettings)
    dashboard = Column(AccountDashboardSettings)
    payments = Column(AccountPaymentsSettings)
    payouts = Column(AccountPayoutSettings, nullable=True)
    sepa_debit_payments = Column(AccountSepaDebitPaymentsSettings, nullable=True)
    treasury = Column(AccountTreasurySettings, nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance
        
        :return: String representation of instance
        :rtype: ```str```
        """
        return 'Account_Settings(bacs_debit_payments={bacs_debit_payments!r}, branding={branding!r}, card_issuing={card_issuing!r}, card_payments={card_payments!r}, dashboard={dashboard!r}, payments={payments!r}, payouts={payouts!r}, sepa_debit_payments={sepa_debit_payments!r}, treasury={treasury!r}, id={id!r})'.format(bacs_debit_payments=self.bacs_debit_payments, branding=self.branding, card_issuing=self.card_issuing, card_payments=self.card_payments, dashboard=self.dashboard, payments=self.payments, payouts=self.payouts, sepa_debit_payments=self.sepa_debit_payments, treasury=self.treasury, id=self.id)
__all__ = ['account_settings']