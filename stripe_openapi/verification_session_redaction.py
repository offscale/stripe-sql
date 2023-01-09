from sqlalchemy import Column, Identity, Integer, String

from . import Base


class VerificationSessionRedaction(Base):
    __tablename__ = "verification_session_redaction"
    status = Column(
        String,
        comment="Indicates whether this object and its related objects have been redacted or not",
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "VerificationSessionRedaction(status={status!r}, id={id!r})".format(
            status=self.status, id=self.id
        )


__all__ = ["verification_session_redaction"]
