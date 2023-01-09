from sqlalchemy import Column, Identity, Integer, String

from . import Base


class MandateSingleUse(Base):
    __tablename__ = "mandate_single_use"
    amount = Column(
        Integer, comment="On a single use mandate, the amount of the payment"
    )
    currency = Column(
        String, comment="On a single use mandate, the currency of the payment"
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "MandateSingleUse(amount={amount!r}, currency={currency!r}, id={id!r})".format(
            amount=self.amount, currency=self.currency, id=self.id
        )


__all__ = ["mandate_single_use"]
