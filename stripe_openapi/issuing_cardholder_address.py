from sqlalchemy import Column, ForeignKey, Identity, Integer, Table

from stripe_openapi.address import Address

from . import metadata

IssuingCardholderAddressJson = Table(
    "issuing_cardholder_addressjson",
    metadata,
    Column("address", Address, ForeignKey("Address")),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["issuing_cardholder_address.json"]
