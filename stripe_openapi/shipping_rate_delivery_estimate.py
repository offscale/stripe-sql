from sqlalchemy import Column, Identity, Integer

from stripe_openapi.shipping_rate_delivery_estimate_bound import (
    ShippingRateDeliveryEstimateBound,
)

from . import Base


class ShippingRateDeliveryEstimate(Base):
    __tablename__ = "shipping_rate_delivery_estimate"
    maximum = Column(
        ShippingRateDeliveryEstimateBound,
        comment="[[FK(ShippingRateDeliveryEstimateBound)]] The upper bound of the estimated range. If empty, represents no upper bound i.e., infinite",
        nullable=True,
    )
    minimum = Column(
        ShippingRateDeliveryEstimateBound,
        comment="[[FK(ShippingRateDeliveryEstimateBound)]] The lower bound of the estimated range. If empty, represents no lower bound",
        nullable=True,
    )
    id = Column(Integer, primary_key=True, server_default=Identity())

    def __repr__(self):
        """
        Emit a string representation of the current instance

        :return: String representation of instance
        :rtype: ```str```
        """
        return "ShippingRateDeliveryEstimate(maximum={maximum!r}, minimum={minimum!r}, id={id!r})".format(
            maximum=self.maximum, minimum=self.minimum, id=self.id
        )


__all__ = ["shipping_rate_delivery_estimate"]
