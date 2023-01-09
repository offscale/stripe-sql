from sqlalchemy import Column, Identity, Integer, String

from . import Base


class TreasuryFinancialAccountsResourceAbaRecord(Base):
    """
    ABA Records contain U.S. bank account details per the ABA format.
    """

    __tablename__ = "treasury_financial_accounts_resource_aba_record"
    account_holder_name = Column(
        String, comment="The name of the person or business that owns the bank account"
    )
    account_number = Column(String, comment="The account number", nullable=True)
    account_number_last4 = Column(
        String, comment="The last four characters of the account number"
    )
    bank_name = Column(String, comment="Name of the bank")
    routing_number = Column(String, comment="Routing number for the account")
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "TreasuryFinancialAccountsResourceAbaRecord(account_holder_name={account_holder_name!r}, account_number={account_number!r}, account_number_last4={account_number_last4!r}, bank_name={bank_name!r}, routing_number={routing_number!r}, id={id!r})".format(
            account_holder_name=self.account_holder_name,
            account_number=self.account_number,
            account_number_last4=self.account_number_last4,
            bank_name=self.bank_name,
            routing_number=self.routing_number,
            id=self.id,
        )


__all__ = ["treasury_financial_accounts_resource_aba_record"]
