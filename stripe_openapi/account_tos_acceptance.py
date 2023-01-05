from sqlalchemy import Column, Integer, String


class Account_Tos_Acceptance(Base):
    __tablename__ = "account_tos_acceptance"
    date = Column(
        Integer,
        comment="The Unix timestamp marking when the account representative accepted their service agreement",
        nullable=True,
    )
    ip = Column(
        String,
        comment="The IP address from which the account representative accepted their service agreement",
        nullable=True,
    )
    service_agreement = Column(
        String, comment="The user's service agreement type", nullable=True
    )
    user_agent = Column(
        String,
        comment="The user agent of the browser from which the account representative accepted their service agreement",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Account_Tos_Acceptance(date={date!r}, ip={ip!r}, service_agreement={service_agreement!r}, user_agent={user_agent!r}, id={id!r})".format(
            date=self.date,
            ip=self.ip,
            service_agreement=self.service_agreement,
            user_agent=self.user_agent,
            id=self.id,
        )


__all__ = ["account_tos_acceptance"]
