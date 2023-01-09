from sqlalchemy import ARRAY, Column, ForeignKey, Identity, Integer, String

from . import Base


class FundingInstructionsBankTransferFinancialAddress(Base):
    """
    FinancialAddresses contain identifying information that resolves to a FinancialAccount.
    """

    __tablename__ = "funding_instructions_bank_transfer_financial_address"
    iban = Column(
        String,
        ForeignKey(
            "funding_instructions_bank_transfer_iban_record.account_holder_name"
        ),
        nullable=True,
    )
    sort_code = Column(
        String,
        ForeignKey(
            "funding_instructions_bank_transfer_sort_code_record.account_holder_name"
        ),
        nullable=True,
    )
    spei = Column(
        String,
        ForeignKey("funding_instructions_bank_transfer_spei_record.bank_name"),
        nullable=True,
    )
    supported_networks = Column(
        ARRAY(String),
        comment="The payment networks supported by this FinancialAddress",
        nullable=True,
    )
    type = Column(String, comment="The type of financial address")
    zengin = Column(
        Integer,
        ForeignKey("funding_instructions_bank_transfer_zengin_record.id"),
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "FundingInstructionsBankTransferFinancialAddress(iban={iban!r}, sort_code={sort_code!r}, spei={spei!r}, supported_networks={supported_networks!r}, type={type!r}, zengin={zengin!r}, id={id!r})".format(
            iban=self.iban,
            sort_code=self.sort_code,
            spei=self.spei,
            supported_networks=self.supported_networks,
            type=self.type,
            zengin=self.zengin,
            id=self.id,
        )


__all__ = ["funding_instructions_bank_transfer_financial_address"]
