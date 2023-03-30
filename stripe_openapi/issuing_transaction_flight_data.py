from sqlalchemy import Boolean, Column, Integer, String, Table, list

from . import metadata

IssuingTransactionFlightData.Json = Table(
    "issuing_transaction_flight_data.json",
    metadata,
    Column(
        "departure_at",
        Integer,
        comment="The time that the flight departed",
        nullable=True,
    ),
    Column(
        "passenger_name",
        String,
        comment="The name of the passenger",
        nullable=True,
        primary_key=True,
    ),
    Column(
        "refundable", Boolean, comment="Whether the ticket is refundable", nullable=True
    ),
    Column("segments", list, comment="The legs of the trip", nullable=True),
    Column(
        "travel_agency",
        String,
        comment="The travel agency that issued the ticket",
        nullable=True,
    ),
)
__all__ = ["issuing_transaction_flight_data.json"]
