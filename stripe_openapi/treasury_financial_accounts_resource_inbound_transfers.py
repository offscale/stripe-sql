from sqlalchemy import Column, ForeignKey, Identity, Integer

from . import Base


class TreasuryFinancialAccountsResourceInboundTransfers(Base):
    """
    InboundTransfers contains inbound transfers features for a FinancialAccount.
    """

    __tablename__ = "treasury_financial_accounts_resource_inbound_transfers"
    ach = Column(
        Integer,
        ForeignKey("treasury_financial_accounts_resource_ach_toggle_settings.id"),
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "TreasuryFinancialAccountsResourceInboundTransfers(ach={ach!r}, id={id!r})".format(
            ach=self.ach, id=self.id
        )


__all__ = ["treasury_financial_accounts_resource_inbound_transfers"]
