from sqlalchemy import ARRAY, Column, ForeignKey, Identity, Integer, String

from . import Base


class TreasuryFinancialAccountsResourceFinancialAddress(Base):
    """
    FinancialAddresses contain identifying information that resolves to a FinancialAccount.
    """

    __tablename__ = "treasury_financial_accounts_resource_financial_address"
    aba = Column(
        Integer,
        ForeignKey("treasury_financial_accounts_resource_aba_record.id"),
        nullable=True,
    )
    supported_networks = Column(
        ARRAY(String),
        comment="The list of networks that the address supports",
        nullable=True,
    )
    type = Column(String, comment="The type of financial address")
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "TreasuryFinancialAccountsResourceFinancialAddress(aba={aba!r}, supported_networks={supported_networks!r}, type={type!r}, id={id!r})".format(
            aba=self.aba,
            supported_networks=self.supported_networks,
            type=self.type,
            id=self.id,
        )


__all__ = ["treasury_financial_accounts_resource_financial_address"]
