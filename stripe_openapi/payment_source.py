from sqlalchemy import Column, Identity, Integer

from . import Base


class PaymentSource(Base):
    __tablename__ = "payment_source"
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "PaymentSource(id={id!r})".format(id=self.id)


__all__ = ["payment_source"]
