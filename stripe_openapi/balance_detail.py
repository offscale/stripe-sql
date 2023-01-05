from sqlalchemy import Column, Integer


class Balance_Detail(Base):
    __tablename__ = "balance_detail"
    available = Column(list, comment="Funds that are available for use")
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Balance_Detail(available={available!r}, id={id!r})".format(
            available=self.available, id=self.id
        )


__all__ = ["balance_detail"]
