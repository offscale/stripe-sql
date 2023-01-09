from sqlalchemy import Column, Identity, Integer, String

from . import Base


class GelatoSessionLastError(Base):
    """
    Shows last VerificationSession error
    """

    __tablename__ = "gelato_session_last_error"
    code = Column(
        String,
        comment="A short machine-readable string giving the reason for the verification or user-session failure",
        nullable=True,
    )
    reason = Column(
        String,
        comment="A message that explains the reason for verification or user-session failure",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "GelatoSessionLastError(code={code!r}, reason={reason!r}, id={id!r})".format(
            code=self.code, reason=self.reason, id=self.id
        )


__all__ = ["gelato_session_last_error"]
