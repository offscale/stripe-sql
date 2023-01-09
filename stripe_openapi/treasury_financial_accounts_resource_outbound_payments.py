from sqlalchemy import Column, ForeignKey, Identity, Integer

from . import Base


class TreasuryFinancialAccountsResourceOutboundPayments(Base):
    """
    Settings related to Outbound Payments features on a Financial Account
    """

    __tablename__ = "treasury_financial_accounts_resource_outbound_payments"
    ach = Column(
        Integer,
        ForeignKey("treasury_financial_accounts_resource_ach_toggle_settings.id"),
        nullable=True,
    )
    us_domestic_wire = Column(
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
        return "TreasuryFinancialAccountsResourceOutboundPayments(ach={ach!r}, us_domestic_wire={us_domestic_wire!r}, id={id!r})".format(
            ach=self.ach, us_domestic_wire=self.us_domestic_wire, id=self.id
        )


__all__ = ["treasury_financial_accounts_resource_outbound_payments"]
