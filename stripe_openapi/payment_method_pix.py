from sqlalchemy import Column, Identity, Integer

from . import Base


class PaymentMethodPix(Base):
    __tablename__ = "payment_method_pix"
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "PaymentMethodPix(id={id!r})".format(id=self.id)


__all__ = ["payment_method_pix"]
