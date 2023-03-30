from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

TransformUsage.Json = Table(
    "transform_usage.json",
    metadata,
    Column("divide_by", Integer, comment="Divide usage by this number"),
    Column(
        "round",
        String,
        comment="After division, either round the result `up` or `down`",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["transform_usage.json"]
