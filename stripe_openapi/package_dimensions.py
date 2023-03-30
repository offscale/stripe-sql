from sqlalchemy import Column, Float, Identity, Integer, Table

from . import metadata

PackageDimensions.Json = Table(
    "package_dimensions.json",
    metadata,
    Column("height", Float, comment="Height, in inches"),
    Column("length", Float, comment="Length, in inches"),
    Column("weight", Float, comment="Weight, in ounces"),
    Column("width", Float, comment="Width, in inches"),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["package_dimensions.json"]
