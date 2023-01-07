from sqlalchemy import Column, Integer, String


class Funding_Instructions_Bank_Transfer_Financial_Address(Base):
    """
    FinancialAddresses contain identifying information that resolves to a FinancialAccount.
    """

    __tablename__ = "funding_instructions_bank_transfer_financial_address"
    iban = Column(
        funding_instructions_bank_transfer_iban_record,
        ForeignKey("funding_instructions_bank_transfer_iban_record"),
        nullable=True,
    )
    sort_code = Column(
        funding_instructions_bank_transfer_sort_code_record,
        ForeignKey("funding_instructions_bank_transfer_sort_code_record"),
        nullable=True,
    )
    spei = Column(
        funding_instructions_bank_transfer_spei_record,
        ForeignKey("funding_instructions_bank_transfer_spei_record"),
        nullable=True,
    )
    supported_networks = Column(
        ARRAY(String),
        comment="The payment networks supported by this FinancialAddress",
        nullable=True,
    )
    type = Column(String, comment="The type of financial address")
    zengin = Column(
        funding_instructions_bank_transfer_zengin_record,
        ForeignKey("funding_instructions_bank_transfer_zengin_record"),
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Funding_Instructions_Bank_Transfer_Financial_Address(iban={iban!r}, sort_code={sort_code!r}, spei={spei!r}, supported_networks={supported_networks!r}, type={type!r}, zengin={zengin!r}, id={id!r})".format(
            iban=self.iban,
            sort_code=self.sort_code,
            spei=self.spei,
            supported_networks=self.supported_networks,
            type=self.type,
            zengin=self.zengin,
            id=self.id,
        )


__all__ = ["funding_instructions_bank_transfer_financial_address"]
