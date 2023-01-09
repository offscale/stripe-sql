from sqlalchemy import Column, Identity, Integer, String

from . import Base


class BankConnectionsResourceOwnershipRefresh(Base):
    __tablename__ = "bank_connections_resource_ownership_refresh"
    last_attempted_at = Column(
        Integer,
        comment="The time at which the last refresh attempt was initiated. Measured in seconds since the Unix epoch",
    )
    status = Column(String, comment="The status of the last refresh attempt")
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "BankConnectionsResourceOwnershipRefresh(last_attempted_at={last_attempted_at!r}, status={status!r}, id={id!r})".format(
            last_attempted_at=self.last_attempted_at, status=self.status, id=self.id
        )


__all__ = ["bank_connections_resource_ownership_refresh"]
