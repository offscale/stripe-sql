from sqlalchemy import Boolean, Column, Identity, Integer, Table

from . import metadata

ThreeDSecureUsageJson = Table(
    "three_d_secure_usagejson",
    metadata,
    Column("supported", Boolean, comment="Whether 3D Secure is supported on this card"),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["three_d_secure_usage.json"]
