from sqlalchemy import Column, String

from . import Base


class AccountBacsDebitPaymentsSettings(Base):
    __tablename__ = "account_bacs_debit_payments_settings"
    display_name = Column(
        String,
        comment="The Bacs Direct Debit Display Name for this account. For payments made with Bacs Direct Debit, this will appear on the mandate, and as the statement descriptor",
        nullable=True,
        primary_key=True,
    )

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "AccountBacsDebitPaymentsSettings(display_name={display_name!r})".format(
            display_name=self.display_name
        )


__all__ = ["account_bacs_debit_payments_settings"]
