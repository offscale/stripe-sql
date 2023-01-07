from sqlalchemy import Column, Integer


class Account_Settings(Base):
    __tablename__ = "account_settings"
    bacs_debit_payments = Column(
        account_bacs_debit_payments_settings,
        ForeignKey("account_bacs_debit_payments_settings"),
        nullable=True,
    )
    branding = Column(
        account_branding_settings, ForeignKey("account_branding_settings")
    )
    card_issuing = Column(
        account_card_issuing_settings,
        ForeignKey("account_card_issuing_settings"),
        nullable=True,
    )
    card_payments = Column(
        account_card_payments_settings, ForeignKey("account_card_payments_settings")
    )
    dashboard = Column(
        account_dashboard_settings, ForeignKey("account_dashboard_settings")
    )
    payments = Column(
        account_payments_settings, ForeignKey("account_payments_settings")
    )
    payouts = Column(
        account_payout_settings, ForeignKey("account_payout_settings"), nullable=True
    )
    sepa_debit_payments = Column(
        account_sepa_debit_payments_settings,
        ForeignKey("account_sepa_debit_payments_settings"),
        nullable=True,
    )
    treasury = Column(
        account_treasury_settings,
        ForeignKey("account_treasury_settings"),
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Account_Settings(bacs_debit_payments={bacs_debit_payments!r}, branding={branding!r}, card_issuing={card_issuing!r}, card_payments={card_payments!r}, dashboard={dashboard!r}, payments={payments!r}, payouts={payouts!r}, sepa_debit_payments={sepa_debit_payments!r}, treasury={treasury!r}, id={id!r})".format(
            bacs_debit_payments=self.bacs_debit_payments,
            branding=self.branding,
            card_issuing=self.card_issuing,
            card_payments=self.card_payments,
            dashboard=self.dashboard,
            payments=self.payments,
            payouts=self.payouts,
            sepa_debit_payments=self.sepa_debit_payments,
            treasury=self.treasury,
            id=self.id,
        )


__all__ = ["account_settings"]
