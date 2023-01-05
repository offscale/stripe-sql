from sqlalchemy import Column, Integer, String


class Issuing_Transaction_Purchase_Details(Base):
    __tablename__ = "issuing_transaction_purchase_details"
    flight = Column(
        IssuingTransactionFlightData,
        comment="Information about the flight that was purchased with this transaction",
        nullable=True,
    )
    fuel = Column(
        IssuingTransactionFuelData,
        comment="Information about fuel that was purchased with this transaction",
        nullable=True,
    )
    lodging = Column(
        IssuingTransactionLodgingData,
        comment="Information about lodging that was purchased with this transaction",
        nullable=True,
    )
    receipt = Column(list, comment="The line items in the purchase", nullable=True)
    reference = Column(
        String, comment="A merchant-specific order number", nullable=True
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Issuing_Transaction_Purchase_Details(flight={flight!r}, fuel={fuel!r}, lodging={lodging!r}, receipt={receipt!r}, reference={reference!r}, id={id!r})".format(
            flight=self.flight,
            fuel=self.fuel,
            lodging=self.lodging,
            receipt=self.receipt,
            reference=self.reference,
            id=self.id,
        )


__all__ = ["issuing_transaction_purchase_details"]
