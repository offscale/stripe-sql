from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

IssuingCardholderIndividualDob.Json = Table(
    "issuing_cardholder_individual_dob.json",
    metadata,
    Column("day", Integer, comment="The day of birth, between 1 and 31", nullable=True),
    Column(
        "month", Integer, comment="The month of birth, between 1 and 12", nullable=True
    ),
    Column("year", Integer, comment="The four-digit year of birth", nullable=True),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["issuing_cardholder_individual_dob.json"]
