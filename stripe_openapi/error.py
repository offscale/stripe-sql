from sqlalchemy import Column, Integer


class Error(Base):
    """
    An error response from the Stripe API
    """

    __tablename__ = "error"
    error = Column(api_errors, ForeignKey("api_errors"))
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Error(error={error!r}, id={id!r})".format(error=self.error, id=self.id)


__all__ = ["error"]
