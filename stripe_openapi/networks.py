from sqlalchemy import Column, Integer, String


class Networks(Base):
    __tablename__ = "networks"
    available = Column(ARRAY(String), comment="All available networks for the card")
    preferred = Column(
        String, comment="The preferred network for the card", nullable=True
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Networks(available={available!r}, preferred={preferred!r}, id={id!r})".format(
            available=self.available, preferred=self.preferred, id=self.id
        )


__all__ = ["networks"]
