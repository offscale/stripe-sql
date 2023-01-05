from sqlalchemy import Column, Integer, String


class Card_Issuing_Account_Terms_Of_Service(Base):
    __tablename__ = "card_issuing_account_terms_of_service"
    date = Column(
        Integer,
        comment="The Unix timestamp marking when the account representative accepted the service agreement",
        nullable=True,
    )
    ip = Column(
        String,
        comment="The IP address from which the account representative accepted the service agreement",
        nullable=True,
    )
    user_agent = Column(
        String,
        comment="The user agent of the browser from which the account representative accepted the service agreement",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Card_Issuing_Account_Terms_Of_Service(date={date!r}, ip={ip!r}, user_agent={user_agent!r}, id={id!r})".format(
            date=self.date, ip=self.ip, user_agent=self.user_agent, id=self.id
        )


__all__ = ["card_issuing_account_terms_of_service"]
