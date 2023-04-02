from sqlalchemy import Column, ForeignKey, Identity, Integer, Table

from . import metadata

ShippingRateDeliveryEstimateJson = Table(
    "shipping_rate_delivery_estimatejson",
    metadata,
    Column(
        "maximum",
        ShippingRateDeliveryEstimateBound,
        ForeignKey("ShippingRateDeliveryEstimateBound"),
        comment="The upper bound of the estimated range. If empty, represents no upper bound i.e., infinite",
        nullable=True,
    ),
    Column(
        "minimum",
        ShippingRateDeliveryEstimateBound,
        ForeignKey("ShippingRateDeliveryEstimateBound"),
        comment="The lower bound of the estimated range. If empty, represents no lower bound",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["shipping_rate_delivery_estimate.json"]
