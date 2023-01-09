from sqlalchemy import Column, Identity, Integer, String

from . import Base


class IssuingCardholderUserTermsAcceptance(Base):
    __tablename__ = "issuing_cardholder_user_terms_acceptance"
    date = Column(
        Integer,
        comment="The Unix timestamp marking when the cardholder accepted the Authorized User Terms",
        nullable=True,
    )
    ip = Column(
        String,
        comment="The IP address from which the cardholder accepted the Authorized User Terms",
        nullable=True,
    )
    user_agent = Column(
        String,
        comment="The user agent of the browser from which the cardholder accepted the Authorized User Terms",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "IssuingCardholderUserTermsAcceptance(date={date!r}, ip={ip!r}, user_agent={user_agent!r}, id={id!r})".format(
            date=self.date, ip=self.ip, user_agent=self.user_agent, id=self.id
        )


__all__ = ["issuing_cardholder_user_terms_acceptance"]
