from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

RadarRadarOptions.Json = Table(
    "radar_radar_options.json",
    metadata,
    Column(
        "session",
        String,
        comment="A [Radar Session](https://stripe.com/docs/radar/radar-session) is a snapshot of the browser metadata and device details that help Radar make more accurate predictions on your payments",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["radar_radar_options.json"]
