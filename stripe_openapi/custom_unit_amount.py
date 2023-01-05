from sqlalchemy import Column, Integer


class Custom_Unit_Amount(Base):
    __tablename__ = "custom_unit_amount"
    maximum = Column(
        Integer,
        comment="The maximum unit amount the customer can specify for this item",
        nullable=True,
    )
    minimum = Column(
        Integer,
        comment="The minimum unit amount the customer can specify for this item. Must be at least the minimum charge amount",
        nullable=True,
    )
    preset = Column(
        Integer,
        comment="The starting unit amount which can be updated by the customer",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Custom_Unit_Amount(maximum={maximum!r}, minimum={minimum!r}, preset={preset!r}, id={id!r})".format(
            maximum=self.maximum, minimum=self.minimum, preset=self.preset, id=self.id
        )


__all__ = ["custom_unit_amount"]
