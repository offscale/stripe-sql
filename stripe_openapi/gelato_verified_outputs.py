from sqlalchemy import Column, ForeignKey, Identity, Integer, String, Table

from stripe_openapi.address import Address

from . import metadata

GelatoVerifiedOutputs.Json = Table(
    "gelato_verified_outputs.json",
    metadata,
    Column(
        "address",
        Address,
        ForeignKey("Address"),
        comment="The user's verified address",
        nullable=True,
    ),
    Column(
        "dob",
        GelatoDataVerifiedOutputsDate,
        ForeignKey("GelatoDataVerifiedOutputsDate"),
        comment="The user’s verified date of birth",
        nullable=True,
    ),
    Column(
        "first_name", String, comment="The user's verified first name", nullable=True
    ),
    Column("id_number", String, comment="The user's verified id number", nullable=True),
    Column(
        "id_number_type",
        String,
        comment="The user's verified id number type",
        nullable=True,
    ),
    Column("last_name", String, comment="The user's verified last name", nullable=True),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["gelato_verified_outputs.json"]
