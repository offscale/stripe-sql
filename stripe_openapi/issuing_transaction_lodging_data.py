from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

IssuingTransactionLodgingData.Json = Table(
    "issuing_transaction_lodging_data.json",
    metadata,
    Column(
        "check_in_at",
        Integer,
        comment="The time of checking into the lodging",
        nullable=True,
    ),
    Column(
        "nights",
        Integer,
        comment="The number of nights stayed at the lodging",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["issuing_transaction_lodging_data.json"]
