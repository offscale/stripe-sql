from sqlalchemy import Column, ForeignKey, Identity, Integer

from . import Base


class TransferData(Base):
    __tablename__ = "transfer_data"
    amount = Column(
        Integer,
        comment="Amount intended to be collected by this PaymentIntent. A positive integer representing how much to charge in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal) (e.g., 100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal currency). The minimum amount is $0.50 US or [equivalent in charge currency](https://stripe.com/docs/currencies#minimum-and-maximum-charge-amounts). The amount value supports up to eight digits (e.g., a value of 99999999 for a USD charge of $999,999.99)",
        nullable=True,
    )
    destination = Column(
        Account,
        ForeignKey("Account"),
        comment="The account (if any) the payment will be attributed to for tax\nreporting, and where funds from the payment will be transferred to upon\npayment success",
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "TransferData(amount={amount!r}, destination={destination!r}, id={id!r})".format(
            amount=self.amount, destination=self.destination, id=self.id
        )


__all__ = ["transfer_data"]
