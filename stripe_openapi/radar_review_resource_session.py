from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

RadarReviewResourceSessionJson = Table(
    "radar_review_resource_sessionjson",
    metadata,
    Column(
        "browser",
        String,
        comment="The browser used in this browser session (e.g., `Chrome`)",
        nullable=True,
    ),
    Column(
        "device",
        String,
        comment="Information about the device used for the browser session (e.g., `Samsung SM-G930T`)",
        nullable=True,
    ),
    Column(
        "platform",
        String,
        comment="The platform for the browser session (e.g., `Macintosh`)",
        nullable=True,
    ),
    Column(
        "version",
        String,
        comment="The version for the browser session (e.g., `61.0.3163.100`)",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["radar_review_resource_session.json"]
