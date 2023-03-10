from sqlalchemy import Column, ForeignKey, Identity, Integer

from . import Base


class AccountCardIssuingSettings(Base):
    __tablename__ = "account_card_issuing_settings"
    tos_acceptance = Column(
        Integer, ForeignKey("card_issuing_account_terms_of_service.id"), nullable=True
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "AccountCardIssuingSettings(tos_acceptance={tos_acceptance!r}, id={id!r})".format(
            tos_acceptance=self.tos_acceptance, id=self.id
        )


__all__ = ["account_card_issuing_settings"]
