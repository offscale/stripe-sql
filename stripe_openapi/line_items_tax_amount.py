from sqlalchemy import Column, ForeignKey, Identity, Integer

from . import Base


class LineItemsTaxAmount(Base):
    __tablename__ = "line_items_tax_amount"
    amount = Column(Integer, comment="Amount of tax applied for this rate")
    rate = Column(String, ForeignKey("tax_rate.id"))
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "LineItemsTaxAmount(amount={amount!r}, rate={rate!r}, id={id!r})".format(
            amount=self.amount, rate=self.rate, id=self.id
        )


__all__ = ["line_items_tax_amount"]
