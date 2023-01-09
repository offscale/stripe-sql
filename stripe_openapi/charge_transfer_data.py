from sqlalchemy import Column, Identity, Integer

from . import Base


class ChargeTransferData(Base):
    __tablename__ = "charge_transfer_data"
    amount = Column(
        Integer,
        comment="The amount transferred to the destination account, if specified. By default, the entire charge amount is transferred to the destination account",
        nullable=True,
    )
    destination = Column(
        Account,
        comment="[[FK(Account)]] ID of an existing, connected Stripe account to transfer funds to if `transfer_data` was specified in the charge request",
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "ChargeTransferData(amount={amount!r}, destination={destination!r}, id={id!r})".format(
            amount=self.amount, destination=self.destination, id=self.id
        )


__all__ = ["charge_transfer_data"]
