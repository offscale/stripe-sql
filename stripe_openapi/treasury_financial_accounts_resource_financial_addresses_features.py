from sqlalchemy import Column, Integer


class Treasury_Financial_Accounts_Resource_Financial_Addresses_Features(Base):
    """
    Settings related to Financial Addresses features on a Financial Account
    """

    __tablename__ = "treasury_financial_accounts_resource_financial_addresses_features"
    aba = Column(
        treasury_financial_accounts_resource_toggle_settings,
        ForeignKey("treasury_financial_accounts_resource_toggle_settings"),
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Treasury_Financial_Accounts_Resource_Financial_Addresses_Features(aba={aba!r}, id={id!r})".format(
            aba=self.aba, id=self.id
        )


__all__ = ["treasury_financial_accounts_resource_financial_addresses_features"]
