from sqlalchemy import JSON, Column, String, Table

from . import metadata

ExchangeRateJson = Table(
    "exchange_ratejson",
    metadata,
    Column(
        "id",
        String,
        comment="Unique identifier for the object. Represented as the three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) in lowercase",
        primary_key=True,
    ),
    Column(
        "object",
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    ),
    Column(
        "rates",
        JSON,
        comment="Hash where the keys are supported currencies and the values are the exchange rate at which the base id currency converts to the key currency",
    ),
)
__all__ = ["exchange_rate.json"]
