from sqlalchemy import ARRAY, Column, Identity, Integer, String

from . import Base


class TreasuryFinancialAccountsResourceClosedStatusDetails(Base):
    __tablename__ = "treasury_financial_accounts_resource_closed_status_details"
    reasons = Column(
        ARRAY(String),
        comment="The array that contains reasons for a FinancialAccount closure",
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "TreasuryFinancialAccountsResourceClosedStatusDetails(reasons={reasons!r}, id={id!r})".format(
            reasons=self.reasons, id=self.id
        )


__all__ = ["treasury_financial_accounts_resource_closed_status_details"]
