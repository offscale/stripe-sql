from sqlalchemy import Column, Identity, Integer

from . import Base


class DeletedPaymentSource(Base):
    __tablename__ = "deleted_payment_source"
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "DeletedPaymentSource(id={id!r})".format(id=self.id)


__all__ = ["deleted_payment_source"]
