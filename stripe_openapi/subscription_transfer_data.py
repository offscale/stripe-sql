from sqlalchemy import Column, Float, ForeignKey, Identity, Integer

from . import Base


class SubscriptionTransferData(Base):
    __tablename__ = "subscription_transfer_data"
    amount_percent = Column(
        Float,
        comment="A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice subtotal that will be transferred to the destination account. By default, the entire amount is transferred to the destination",
        nullable=True,
    )
    destination = Column(
        Account,
        ForeignKey("Account"),
        comment="The account where funds from the payment will be transferred to upon payment success",
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "SubscriptionTransferData(amount_percent={amount_percent!r}, destination={destination!r}, id={id!r})".format(
            amount_percent=self.amount_percent, destination=self.destination, id=self.id
        )


__all__ = ["subscription_transfer_data"]
