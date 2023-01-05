from sqlalchemy import Column, Float, Integer, String


class Issuing_Transaction_Receipt_Data(Base):
    __tablename__ = "issuing_transaction_receipt_data"
    description = Column(
        String,
        comment="The description of the item. The maximum length of this field is 26 characters",
        nullable=True,
    )
    quantity = Column(Float, comment="The quantity of the item", nullable=True)
    total = Column(
        Integer, comment="The total for this line item in cents", nullable=True
    )
    unit_cost = Column(
        Integer, comment="The unit cost of the item in cents", nullable=True
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Issuing_Transaction_Receipt_Data(description={description!r}, quantity={quantity!r}, total={total!r}, unit_cost={unit_cost!r}, id={id!r})".format(
            description=self.description,
            quantity=self.quantity,
            total=self.total,
            unit_cost=self.unit_cost,
            id=self.id,
        )


__all__ = ["issuing_transaction_receipt_data"]
