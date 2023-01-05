from sqlalchemy import Column, Integer, String


class Source_Order(Base):
    __tablename__ = "source_order"
    amount = Column(
        Integer,
        comment="A positive integer in the smallest currency unit (that is, 100 cents for $1.00, or 1 for ¥1, Japanese Yen being a zero-decimal currency) representing the total amount for the order",
    )
    currency = Column(
        String,
        comment="Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)",
    )
    email = Column(
        String,
        comment="The email address of the customer placing the order",
        nullable=True,
    )
    items = Column(list, comment="List of items constituting the order", nullable=True)
    shipping = Column(Shipping, nullable=True)
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Source_Order(amount={amount!r}, currency={currency!r}, email={email!r}, items={items!r}, shipping={shipping!r}, id={id!r})".format(
            amount=self.amount,
            currency=self.currency,
            email=self.email,
            items=self.items,
            shipping=self.shipping,
            id=self.id,
        )


__all__ = ["source_order"]
