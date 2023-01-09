from sqlalchemy import ARRAY, Column, Identity, Integer, String

from . import Base


class UsBankAccountNetworks(Base):
    __tablename__ = "us_bank_account_networks"
    preferred = Column(String, comment="The preferred network", nullable=True)
    supported = Column(ARRAY(String), comment="All supported networks")
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "UsBankAccountNetworks(preferred={preferred!r}, supported={supported!r}, id={id!r})".format(
            preferred=self.preferred, supported=self.supported, id=self.id
        )


__all__ = ["us_bank_account_networks"]
