from sqlalchemy import Column, String


class Exchange_Rate(Base):
    """
    `Exchange Rate` objects allow you to determine the rates that Stripe is

    currently using to convert from one currency to another. Since this number is
    variable throughout the day, there are various reasons why you might want to
    know the current rate (for example, to dynamically price an item for a user
    with a default payment in a foreign currency).

    If you want a guarantee that the charge is made with a certain exchange rate
    you expect is current, you can pass in `exchange_rate` to charges endpoints.
    If the value is no longer up to date, the charge won't go through. Please
    refer to our [Exchange Rates API](https://stripe.com/docs/exchange-rates) guide for more
    details.

    """

    __tablename__ = "exchange_rate"
    id = Column(
        String,
        comment="Unique identifier for the object. Represented as the three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) in lowercase",
        primary_key=True,
    )
    object = Column(
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    )
    rates = Column(
        JSON,
        comment="Hash where the keys are supported currencies and the values are the exchange rate at which the base id currency converts to the key currency",
    )

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Exchange_Rate(id={id!r}, object={object!r}, rates={rates!r})".format(
            id=self.id, object=self.object, rates=self.rates
        )


__all__ = ["exchange_rate"]
