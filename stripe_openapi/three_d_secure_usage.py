from sqlalchemy import Boolean, Column, Identity, Integer

from . import Base


class ThreeDSecureUsage(Base):
    __tablename__ = "three_d_secure_usage"
    supported = Column(Boolean, comment="Whether 3D Secure is supported on this card")
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "ThreeDSecureUsage(supported={supported!r}, id={id!r})".format(
            supported=self.supported, id=self.id
        )


__all__ = ["three_d_secure_usage"]
