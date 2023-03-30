from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

Period.Json = Table(
    "period.json",
    metadata,
    Column(
        "end",
        Integer,
        comment="The end date of this usage period. All usage up to and including this point in time is included",
        nullable=True,
    ),
    Column(
        "start",
        Integer,
        comment="The start date of this usage period. All usage after this point in time is included",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["period.json"]
