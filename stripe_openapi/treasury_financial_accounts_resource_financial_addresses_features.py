from sqlalchemy import Column, ForeignKey, Identity, Integer

from . import Base


class TreasuryFinancialAccountsResourceFinancialAddressesFeatures(Base):
    """
    Settings related to Financial Addresses features on a Financial Account
    """

    __tablename__ = "treasury_financial_accounts_resource_financial_addresses_features"
    aba = Column(
        Integer,
        ForeignKey("treasury_financial_accounts_resource_toggle_settings.id"),
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "TreasuryFinancialAccountsResourceFinancialAddressesFeatures(aba={aba!r}, id={id!r})".format(
            aba=self.aba, id=self.id
        )


__all__ = ["treasury_financial_accounts_resource_financial_addresses_features"]
