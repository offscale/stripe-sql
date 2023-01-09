from sqlalchemy import Column, ForeignKey, Identity, Integer

from . import Base


class Error(Base):
    """
    An error response from the Stripe API
    """

    __tablename__ = "error"
    error = Column(Integer, ForeignKey("api_errors.id"))
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Error(error={error!r}, id={id!r})".format(error=self.error, id=self.id)


__all__ = ["error"]
