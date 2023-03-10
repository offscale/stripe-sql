from sqlalchemy import Column, Identity, Integer

from . import Base


class PaymentMethodCustomerBalance(Base):
    __tablename__ = "payment_method_customer_balance"
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "PaymentMethodCustomerBalance(id={id!r})".format(id=self.id)


__all__ = ["payment_method_customer_balance"]
