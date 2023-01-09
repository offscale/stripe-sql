from sqlalchemy import Column, Identity, Integer, String

from . import Base


class SigmaScheduledQueryRunError(Base):
    __tablename__ = "sigma_scheduled_query_run_error"
    message = Column(String, comment="Information about the run failure")
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "SigmaScheduledQueryRunError(message={message!r}, id={id!r})".format(
            message=self.message, id=self.id
        )


__all__ = ["sigma_scheduled_query_run_error"]
