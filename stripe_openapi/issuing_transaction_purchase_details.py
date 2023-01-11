from sqlalchemy import Column, ForeignKey, Identity, Integer, String, list

from . import Base


class IssuingTransactionPurchaseDetails(Base):
    __tablename__ = "issuing_transaction_purchase_details"
    flight = Column(
        String,
        ForeignKey("issuing_transaction_flight_data.passenger_name"),
        comment="Information about the flight that was purchased with this transaction",
        nullable=True,
    )
    fuel = Column(
        Integer,
        ForeignKey("issuing_transaction_fuel_data.id"),
        comment="Information about fuel that was purchased with this transaction",
        nullable=True,
    )
    lodging = Column(
        Integer,
        ForeignKey("issuing_transaction_lodging_data.id"),
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
        return "IssuingTransactionPurchaseDetails(flight={flight!r}, fuel={fuel!r}, lodging={lodging!r}, receipt={receipt!r}, reference={reference!r}, id={id!r})".format(
            flight=self.flight,
            fuel=self.fuel,
            lodging=self.lodging,
            receipt=self.receipt,
            reference=self.reference,
            id=self.id,
        )


__all__ = ["issuing_transaction_purchase_details"]
