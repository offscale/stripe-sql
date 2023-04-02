from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

CustomerTaxLocationJson = Table(
    "customer_tax_locationjson",
    metadata,
    Column(
        "country", String, comment="The customer's country as identified by Stripe Tax"
    ),
    Column(
        "source",
        String,
        comment="The data source used to infer the customer's location",
    ),
    Column(
        "state",
        String,
        comment="The customer's state, county, province, or region as identified by Stripe Tax",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["customer_tax_location.json"]
