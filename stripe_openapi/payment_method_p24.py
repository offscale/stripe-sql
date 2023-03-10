from sqlalchemy import Column, Identity, Integer, String

from . import Base


class PaymentMethodP24(Base):
    __tablename__ = "payment_method_p24"
    bank = Column(String, comment="The customer's bank, if provided", nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "PaymentMethodP24(bank={bank!r}, id={id!r})".format(
            bank=self.bank, id=self.id
        )


__all__ = ["payment_method_p24"]
