from sqlalchemy import Column, Identity, Integer, String

from . import Base


class PaymentMethodOptionsCustomerBalanceEuBankAccount(Base):
    __tablename__ = "payment_method_options_customer_balance_eu_bank_account"
    country = Column(
        String,
        comment="The desired country code of the bank account information. Permitted values include: `DE`, `ES`, `FR`, `IE`, or `NL`",
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "PaymentMethodOptionsCustomerBalanceEuBankAccount(country={country!r}, id={id!r})".format(
            country=self.country, id=self.id
        )


__all__ = ["payment_method_options_customer_balance_eu_bank_account"]
