from sqlalchemy import Column, Identity, Integer, String

from . import Base


class PlanTier(Base):
    __tablename__ = "plan_tier"
    flat_amount = Column(Integer, comment="Price for the entire tier", nullable=True)
    flat_amount_decimal = Column(
        String,
        comment="Same as `flat_amount`, but contains a decimal value with at most 12 decimal places",
        nullable=True,
    )
    unit_amount = Column(
        Integer, comment="Per unit price for units relevant to the tier", nullable=True
    )
    unit_amount_decimal = Column(
        String,
        comment="Same as `unit_amount`, but contains a decimal value with at most 12 decimal places",
        nullable=True,
    )
    up_to = Column(
        Integer,
        comment="Up to and including to this quantity will be contained in the tier",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "PlanTier(flat_amount={flat_amount!r}, flat_amount_decimal={flat_amount_decimal!r}, unit_amount={unit_amount!r}, unit_amount_decimal={unit_amount_decimal!r}, up_to={up_to!r}, id={id!r})".format(
            flat_amount=self.flat_amount,
            flat_amount_decimal=self.flat_amount_decimal,
            unit_amount=self.unit_amount,
            unit_amount_decimal=self.unit_amount_decimal,
            up_to=self.up_to,
            id=self.id,
        )


__all__ = ["plan_tier"]
