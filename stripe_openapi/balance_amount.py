from sqlalchemy import Column, ForeignKey, Identity, Integer, String

from . import Base


class BalanceAmount(Base):
    __tablename__ = "balance_amount"
    amount = Column(Integer, comment="Balance amount")
    currency = Column(
        String,
        comment="Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)",
    )
    source_types = Column(
        Integer, ForeignKey("balance_amount_by_source_type.id"), nullable=True
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "BalanceAmount(amount={amount!r}, currency={currency!r}, source_types={source_types!r}, id={id!r})".format(
            amount=self.amount,
            currency=self.currency,
            source_types=self.source_types,
            id=self.id,
        )


__all__ = ["balance_amount"]
