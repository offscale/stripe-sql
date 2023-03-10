from sqlalchemy import Boolean, Column, ForeignKey, Identity, Integer, String

from . import Base


class AccountPayoutSettings(Base):
    __tablename__ = "account_payout_settings"
    debit_negative_balances = Column(
        Boolean,
        comment="A Boolean indicating if Stripe should try to reclaim negative balances from an attached bank account. See our [Understanding Connect Account Balances](https://stripe.com/docs/connect/account-balances) documentation for details. Default value is `false` for Custom accounts, otherwise `true`",
    )
    schedule = Column(Integer, ForeignKey("transfer_schedule.id"))
    statement_descriptor = Column(
        String,
        comment="The text that appears on the bank account statement for payouts. If not set, this defaults to the platform's bank descriptor as set in the Dashboard",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "AccountPayoutSettings(debit_negative_balances={debit_negative_balances!r}, schedule={schedule!r}, statement_descriptor={statement_descriptor!r}, id={id!r})".format(
            debit_negative_balances=self.debit_negative_balances,
            schedule=self.schedule,
            statement_descriptor=self.statement_descriptor,
            id=self.id,
        )


__all__ = ["account_payout_settings"]
