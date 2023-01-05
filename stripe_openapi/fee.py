from sqlalchemy import Column, Integer, String


class Fee(Base):
    __tablename__ = "fee"
    amount = Column(Integer, comment="Amount of the fee, in cents")
    application = Column(
        String,
        comment="ID of the Connect application that earned the fee",
        nullable=True,
    )
    currency = Column(
        String,
        comment="Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)",
    )
    description = Column(
        String,
        comment="An arbitrary string attached to the object. Often useful for displaying to users",
        nullable=True,
    )
    type = Column(
        String,
        comment="Type of the fee, one of: `application_fee`, `stripe_fee` or `tax`",
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Fee(amount={amount!r}, application={application!r}, currency={currency!r}, description={description!r}, type={type!r}, id={id!r})".format(
            amount=self.amount,
            application=self.application,
            currency=self.currency,
            description=self.description,
            type=self.type,
            id=self.id,
        )


__all__ = ["fee"]
