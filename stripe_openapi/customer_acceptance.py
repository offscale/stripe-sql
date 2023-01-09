from sqlalchemy import Column, ForeignKey, Identity, Integer, String

from . import Base


class CustomerAcceptance(Base):
    __tablename__ = "customer_acceptance"
    accepted_at = Column(
        Integer,
        comment="The time at which the customer accepted the Mandate",
        nullable=True,
    )
    offline = Column(Integer, ForeignKey("offline_acceptance.id"), nullable=True)
    online = Column(Integer, ForeignKey("online_acceptance.id"), nullable=True)
    type = Column(
        String,
        comment="The type of customer acceptance information included with the Mandate. One of `online` or `offline`",
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "CustomerAcceptance(accepted_at={accepted_at!r}, offline={offline!r}, online={online!r}, type={type!r}, id={id!r})".format(
            accepted_at=self.accepted_at,
            offline=self.offline,
            online=self.online,
            type=self.type,
            id=self.id,
        )


__all__ = ["customer_acceptance"]
