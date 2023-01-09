from sqlalchemy import Column, Identity, Integer, String

from . import Base


class TreasuryFinancialAccountsResourceTogglesSettingStatusDetails(Base):
    """
    Additional details on the FinancialAccount Features information.
    """

    __tablename__ = (
        "treasury_financial_accounts_resource_toggles_setting_status_details"
    )
    code = Column(
        String,
        comment="Represents the reason why the status is `pending` or `restricted`",
    )
    resolution = Column(
        String,
        comment="Represents what the user should do, if anything, to activate the Feature",
        nullable=True,
    )
    restriction = Column(
        String,
        comment="The `platform_restrictions` that are restricting this Feature",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "TreasuryFinancialAccountsResourceTogglesSettingStatusDetails(code={code!r}, resolution={resolution!r}, restriction={restriction!r}, id={id!r})".format(
            code=self.code,
            resolution=self.resolution,
            restriction=self.restriction,
            id=self.id,
        )


__all__ = ["treasury_financial_accounts_resource_toggles_setting_status_details"]
