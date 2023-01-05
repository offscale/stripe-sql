from sqlalchemy import Column, Integer


class Shipping_Rate_Delivery_Estimate(Base):
    __tablename__ = "shipping_rate_delivery_estimate"
    maximum = Column(
        ShippingRateDeliveryEstimateBound,
        comment="The upper bound of the estimated range. If empty, represents no upper bound i.e., infinite",
        nullable=True,
    )
    minimum = Column(
        ShippingRateDeliveryEstimateBound,
        comment="The lower bound of the estimated range. If empty, represents no lower bound",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "Shipping_Rate_Delivery_Estimate(maximum={maximum!r}, minimum={minimum!r}, id={id!r})".format(
            maximum=self.maximum, minimum=self.minimum, id=self.id
        )


__all__ = ["shipping_rate_delivery_estimate"]
