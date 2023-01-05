from sqlalchemy import Column, Integer


class External_Account(Base):
    __tablename__ = "external_account"
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "External_Account(id={id!r})".format(id=self.id)


__all__ = ["external_account"]
