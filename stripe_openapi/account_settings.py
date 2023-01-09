from sqlalchemy import Column, ForeignKey, Identity, Integer

from . import Base


class AccountSettings(Base):
    __tablename__ = "account_settings"
    bacs_debit_payments = Column(
        String,
        ForeignKey("account_bacs_debit_payments_settings.display_name"),
        nullable=True,
    )
    branding = Column(Integer, ForeignKey("account_branding_settings.id"))
    card_issuing = Column(
        Integer, ForeignKey("account_card_issuing_settings.id"), nullable=True
    )
    card_payments = Column(Integer, ForeignKey("account_card_payments_settings.id"))
    dashboard = Column(String, ForeignKey("account_dashboard_settings.display_name"))
    payments = Column(Integer, ForeignKey("account_payments_settings.id"))
    payouts = Column(Integer, ForeignKey("account_payout_settings.id"), nullable=True)
    sepa_debit_payments = Column(
        String,
        ForeignKey("account_sepa_debit_payments_settings.creditor_id"),
        nullable=True,
    )
    treasury = Column(
        Integer, ForeignKey("account_treasury_settings.id"), nullable=True
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "AccountSettings(bacs_debit_payments={bacs_debit_payments!r}, branding={branding!r}, card_issuing={card_issuing!r}, card_payments={card_payments!r}, dashboard={dashboard!r}, payments={payments!r}, payouts={payouts!r}, sepa_debit_payments={sepa_debit_payments!r}, treasury={treasury!r}, id={id!r})".format(
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
