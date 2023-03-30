from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

IssuingTransactionFuelData.Json = Table(
    "issuing_transaction_fuel_data.json",
    metadata,
    Column(
        "type",
        String,
        comment="The type of fuel that was purchased. One of `diesel`, `unleaded_plus`, `unleaded_regular`, `unleaded_super`, or `other`",
    ),
    Column(
        "unit",
        String,
        comment="The units for `volume_decimal`. One of `us_gallon` or `liter`",
    ),
    Column(
        "unit_cost_decimal",
        String,
        comment="The cost in cents per each unit of fuel, represented as a decimal string with at most 12 decimal places",
    ),
    Column(
        "volume_decimal",
        String,
        comment="The volume of the fuel that was pumped, represented as a decimal string with at most 12 decimal places",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["issuing_transaction_fuel_data.json"]
