from sqlalchemy import Column, Identity, Integer, list

from . import Base


class BalanceDetail(Base):
    __tablename__ = "balance_detail"
    available = Column(list, comment="Funds that are available for use")
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "BalanceDetail(available={available!r}, id={id!r})".format(
            available=self.available, id=self.id
        )


__all__ = ["balance_detail"]
