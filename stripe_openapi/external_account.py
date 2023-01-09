from sqlalchemy import Column, Identity, Integer

from . import Base


class ExternalAccount(Base):
    __tablename__ = "external_account"
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "ExternalAccount(id={id!r})".format(id=self.id)


__all__ = ["external_account"]
