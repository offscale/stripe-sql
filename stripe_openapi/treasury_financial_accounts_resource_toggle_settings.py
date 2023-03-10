from sqlalchemy import Boolean, Column, Identity, Integer, String, list

from . import Base


class TreasuryFinancialAccountsResourceToggleSettings(Base):
    """
    Toggle settings for enabling/disabling a feature
    """

    __tablename__ = "treasury_financial_accounts_resource_toggle_settings"
    requested = Column(
        Boolean, comment="Whether the FinancialAccount should have the Feature"
    )
    status = Column(String, comment="Whether the Feature is operational")
    status_details = Column(
        list,
        comment="Additional details; includes at least one entry when the status is not `active`",
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "TreasuryFinancialAccountsResourceToggleSettings(requested={requested!r}, status={status!r}, status_details={status_details!r}, id={id!r})".format(
            requested=self.requested,
            status=self.status,
            status_details=self.status_details,
            id=self.id,
        )


__all__ = ["treasury_financial_accounts_resource_toggle_settings"]
