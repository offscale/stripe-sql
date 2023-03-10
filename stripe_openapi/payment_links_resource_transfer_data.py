from sqlalchemy import Column, ForeignKey, Identity, Integer

from . import Base


class PaymentLinksResourceTransferData(Base):
    __tablename__ = "payment_links_resource_transfer_data"
    amount = Column(
        Integer,
        comment="The amount in %s that will be transferred to the destination account. By default, the entire amount is transferred to the destination",
        nullable=True,
    )
    destination = Column(
        Account,
        ForeignKey("Account"),
        comment="The connected account receiving the transfer",
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "PaymentLinksResourceTransferData(amount={amount!r}, destination={destination!r}, id={id!r})".format(
            amount=self.amount, destination=self.destination, id=self.id
        )


__all__ = ["payment_links_resource_transfer_data"]
