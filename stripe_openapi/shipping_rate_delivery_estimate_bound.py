from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

ShippingRateDeliveryEstimateBound.Json = Table(
    "shipping_rate_delivery_estimate_bound.json",
    metadata,
    Column("unit", String, comment="A unit of time"),
    Column("value", Integer, comment="Must be greater than 0"),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["shipping_rate_delivery_estimate_bound.json"]
