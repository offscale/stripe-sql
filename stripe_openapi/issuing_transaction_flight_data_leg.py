from sqlalchemy import Boolean, Column, Identity, Integer, String, Table

from . import metadata

IssuingTransactionFlightDataLeg.Json = Table(
    "issuing_transaction_flight_data_leg.json",
    metadata,
    Column(
        "arrival_airport_code",
        String,
        comment="The three-letter IATA airport code of the flight's destination",
        nullable=True,
    ),
    Column("carrier", String, comment="The airline carrier code", nullable=True),
    Column(
        "departure_airport_code",
        String,
        comment="The three-letter IATA airport code that the flight departed from",
        nullable=True,
    ),
    Column("flight_number", String, comment="The flight number", nullable=True),
    Column(
        "service_class", String, comment="The flight's service class", nullable=True
    ),
    Column(
        "stopover_allowed",
        Boolean,
        comment="Whether a stopover is allowed on this flight",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["issuing_transaction_flight_data_leg.json"]
