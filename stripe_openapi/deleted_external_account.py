from sqlalchemy import Column, Identity, Integer

from . import Base


class DeletedExternalAccount(Base):
    __tablename__ = "deleted_external_account"
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "DeletedExternalAccount(id={id!r})".format(id=self.id)


__all__ = ["deleted_external_account"]
