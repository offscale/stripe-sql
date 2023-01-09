from sqlalchemy import Column, Identity, Integer, String

from . import Base


class FundingInstructionsBankTransferZenginRecord(Base):
    """
    Zengin Records contain Japan bank account details per the Zengin format.
    """

    __tablename__ = "funding_instructions_bank_transfer_zengin_record"
    account_holder_name = Column(
        String, comment="The account holder name", nullable=True
    )
    account_number = Column(String, comment="The account number", nullable=True)
    account_type = Column(
        String,
        comment="The bank account type. In Japan, this can only be `futsu` or `toza`",
        nullable=True,
    )
    bank_code = Column(String, comment="The bank code of the account", nullable=True)
    bank_name = Column(String, comment="The bank name of the account", nullable=True)
    branch_code = Column(
        String, comment="The branch code of the account", nullable=True
    )
    branch_name = Column(
        String, comment="The branch name of the account", nullable=True
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "FundingInstructionsBankTransferZenginRecord(account_holder_name={account_holder_name!r}, account_number={account_number!r}, account_type={account_type!r}, bank_code={bank_code!r}, bank_name={bank_name!r}, branch_code={branch_code!r}, branch_name={branch_name!r}, id={id!r})".format(
            account_holder_name=self.account_holder_name,
            account_number=self.account_number,
            account_type=self.account_type,
            bank_code=self.bank_code,
            bank_name=self.bank_name,
            branch_code=self.branch_code,
            branch_name=self.branch_name,
            id=self.id,
        )


__all__ = ["funding_instructions_bank_transfer_zengin_record"]
