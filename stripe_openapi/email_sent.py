from sqlalchemy import Column, Integer, String


class Email_Sent(Base):
    __tablename__ = "email_sent"
    email_sent_at = Column(Integer, comment="The timestamp when the email was sent")
    email_sent_to = Column(String, comment="The recipient's email address")
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Email_Sent(email_sent_at={email_sent_at!r}, email_sent_to={email_sent_to!r}, id={id!r})".format(
            email_sent_at=self.email_sent_at,
            email_sent_to=self.email_sent_to,
            id=self.id,
        )


__all__ = ["email_sent"]
