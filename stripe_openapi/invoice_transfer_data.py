from sqlalchemy import Column, Integer


class Invoice_Transfer_Data(Base):
    __tablename__ = "invoice_transfer_data"
    amount = Column(
        Integer,
        comment="The amount in %s that will be transferred to the destination account when the invoice is paid. By default, the entire amount is transferred to the destination",
        nullable=True,
    )
    destination = Column(
        Account,
        comment="The account where funds from the payment will be transferred to upon payment success",
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Invoice_Transfer_Data(amount={amount!r}, destination={destination!r}, id={id!r})".format(
            amount=self.amount, destination=self.destination, id=self.id
        )


__all__ = ["invoice_transfer_data"]
