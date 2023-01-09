from sqlalchemy import Column, String

from . import Base


class FundingInstructionsBankTransferSpeiRecord(Base):
    """
    SPEI Records contain Mexico bank account details per the SPEI format.
    """

    __tablename__ = "funding_instructions_bank_transfer_spei_record"
    bank_code = Column(String, comment="The three-digit bank code")
    bank_name = Column(
        String, comment="The short banking institution name", primary_key=True
    )
    clabe = Column(String, comment="The CLABE number")

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "FundingInstructionsBankTransferSpeiRecord(bank_code={bank_code!r}, bank_name={bank_name!r}, clabe={clabe!r})".format(
            bank_code=self.bank_code, bank_name=self.bank_name, clabe=self.clabe
        )


__all__ = ["funding_instructions_bank_transfer_spei_record"]
