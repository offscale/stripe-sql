from sqlalchemy import Column, Float, Identity, Integer, String, Table

from . import metadata

RadarReviewResourceLocation.Json = Table(
    "radar_review_resource_location.json",
    metadata,
    Column(
        "city", String, comment="The city where the payment originated", nullable=True
    ),
    Column(
        "country",
        String,
        comment="Two-letter ISO code representing the country where the payment originated",
        nullable=True,
    ),
    Column(
        "latitude",
        Float,
        comment="The geographic latitude where the payment originated",
        nullable=True,
    ),
    Column(
        "longitude",
        Float,
        comment="The geographic longitude where the payment originated",
        nullable=True,
    ),
    Column(
        "region",
        String,
        comment="The state/county/province/region where the payment originated",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["radar_review_resource_location.json"]
