from sqlalchemy import JSON, Column, Identity, Integer, String

from . import Base


class ShippingRateFixedAmount(Base):
    __tablename__ = "shipping_rate_fixed_amount"
    amount = Column(
        Integer,
        comment="A non-negative integer in cents representing how much to charge",
    )
    currency = Column(
        String,
        comment="Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)",
    )
    currency_options = Column(
        JSON,
        comment="Shipping rates defined in each available currency option. Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies)",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "ShippingRateFixedAmount(amount={amount!r}, currency={currency!r}, currency_options={currency_options!r}, id={id!r})".format(
            amount=self.amount,
            currency=self.currency,
            currency_options=self.currency_options,
            id=self.id,
        )


__all__ = ["shipping_rate_fixed_amount"]
