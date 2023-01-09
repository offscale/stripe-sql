from sqlalchemy import Column, ForeignKey, Identity, Integer

from . import Base


class AccountTreasurySettings(Base):
    __tablename__ = "account_treasury_settings"
    tos_acceptance = Column(
        Integer, ForeignKey("account_terms_of_service.id"), nullable=True
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "AccountTreasurySettings(tos_acceptance={tos_acceptance!r}, id={id!r})".format(
            tos_acceptance=self.tos_acceptance, id=self.id
        )


__all__ = ["account_treasury_settings"]
