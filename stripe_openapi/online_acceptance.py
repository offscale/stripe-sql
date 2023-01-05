from sqlalchemy import Column, Integer, String


class Online_Acceptance(Base):
    __tablename__ = "online_acceptance"
    ip_address = Column(
        String,
        comment="The IP address from which the Mandate was accepted by the customer",
        nullable=True,
    )
    user_agent = Column(
        String,
        comment="The user agent of the browser from which the Mandate was accepted by the customer",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Online_Acceptance(ip_address={ip_address!r}, user_agent={user_agent!r}, id={id!r})".format(
            ip_address=self.ip_address, user_agent=self.user_agent, id=self.id
        )


__all__ = ["online_acceptance"]
