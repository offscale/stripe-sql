from sqlalchemy import Column, Integer, String


class Issuing_Card_Spending_Limit(Base):
    __tablename__ = "issuing_card_spending_limit"
    amount = Column(
        Integer,
        comment="Maximum amount allowed to spend per interval. This amount is in the card's currency and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal)",
    )
    categories = Column(
        ARRAY(String),
        comment="Array of strings containing [categories](https://stripe.com/docs/api#issuing_authorization_object-merchant_data-category) this limit applies to. Omitting this field will apply the limit to all categories",
        nullable=True,
    )
    interval = Column(String, comment="Interval (or event) to which the amount applies")
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Issuing_Card_Spending_Limit(amount={amount!r}, categories={categories!r}, interval={interval!r}, id={id!r})".format(
            amount=self.amount,
            categories=self.categories,
            interval=self.interval,
            id=self.id,
        )


__all__ = ["issuing_card_spending_limit"]
