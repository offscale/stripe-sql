from sqlalchemy import Column, Identity, Integer, String

from . import Base


class ShippingRateDeliveryEstimateBound(Base):
    __tablename__ = "shipping_rate_delivery_estimate_bound"
    unit = Column(String, comment="A unit of time")
    value = Column(Integer, comment="Must be greater than 0")
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "ShippingRateDeliveryEstimateBound(unit={unit!r}, value={value!r}, id={id!r})".format(
            unit=self.unit, value=self.value, id=self.id
        )


__all__ = ["shipping_rate_delivery_estimate_bound"]
