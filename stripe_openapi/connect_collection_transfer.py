from sqlalchemy import Boolean, Column, Integer, String

from . import Base


class ConnectCollectionTransfer(Base):
    __tablename__ = "connect_collection_transfer"
    amount = Column(Integer, comment="Amount transferred, in %s")
    currency = Column(
        String,
        comment="Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)",
    )
    destination = Column(
        Account,
        comment="[[FK(Account)]] ID of the account that funds are being collected for",
    )
    id = Column(String, comment="Unique identifier for the object", primary_key=True)
    livemode = Column(
        Boolean,
        comment="Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode",
    )
    object = Column(
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    )

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "ConnectCollectionTransfer(amount={amount!r}, currency={currency!r}, destination={destination!r}, id={id!r}, livemode={livemode!r}, object={object!r})".format(
            amount=self.amount,
            currency=self.currency,
            destination=self.destination,
            id=self.id,
            livemode=self.livemode,
            object=self.object,
        )


__all__ = ["connect_collection_transfer"]
