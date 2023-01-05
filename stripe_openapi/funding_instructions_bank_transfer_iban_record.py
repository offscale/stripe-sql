from sqlalchemy import Column, String


class Funding_Instructions_Bank_Transfer_Iban_Record(Base):
    """
    Iban Records contain E.U. bank account details per the SEPA format.
    """

    __tablename__ = "funding_instructions_bank_transfer_iban_record"
    account_holder_name = Column(
        String,
        comment="The name of the person or business that owns the bank account",
        primary_key=True,
    )
    bic = Column(String, comment="The BIC/SWIFT code of the account")
    country = Column(
        String,
        comment="Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2))",
    )
    iban = Column(String, comment="The IBAN of the account")

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Funding_Instructions_Bank_Transfer_Iban_Record(account_holder_name={account_holder_name!r}, bic={bic!r}, country={country!r}, iban={iban!r})".format(
            account_holder_name=self.account_holder_name,
            bic=self.bic,
            country=self.country,
            iban=self.iban,
        )


__all__ = ["funding_instructions_bank_transfer_iban_record"]
