from sqlalchemy import Column, Integer, String


class Legal_Entity_Ubo_Declaration(Base):
    __tablename__ = "legal_entity_ubo_declaration"
    date = Column(
        Integer,
        comment="The Unix timestamp marking when the beneficial owner attestation was made",
        nullable=True,
    )
    ip = Column(
        String,
        comment="The IP address from which the beneficial owner attestation was made",
        nullable=True,
    )
    user_agent = Column(
        String,
        comment="The user-agent string from the browser where the beneficial owner attestation was made",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Legal_Entity_Ubo_Declaration(date={date!r}, ip={ip!r}, user_agent={user_agent!r}, id={id!r})".format(
            date=self.date, ip=self.ip, user_agent=self.user_agent, id=self.id
        )


__all__ = ["legal_entity_ubo_declaration"]
