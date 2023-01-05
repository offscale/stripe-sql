from sqlalchemy import Column, Integer


class Deleted_External_Account(Base):
    __tablename__ = "deleted_external_account"
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Deleted_External_Account(id={id!r})".format(id=self.id)


__all__ = ["deleted_external_account"]
