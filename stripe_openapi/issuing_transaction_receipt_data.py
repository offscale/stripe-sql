from sqlalchemy import Column, Float, Identity, Integer, String, Table

from . import metadata

IssuingTransactionReceiptDataJson = Table(
    "issuing_transaction_receipt_datajson",
    metadata,
    Column(
        "description",
        String,
        comment="The description of the item. The maximum length of this field is 26 characters",
        nullable=True,
    ),
    Column("quantity", Float, comment="The quantity of the item", nullable=True),
    Column(
        "total", Integer, comment="The total for this line item in cents", nullable=True
    ),
    Column(
        "unit_cost",
        Integer,
        comment="The unit cost of the item in cents",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["issuing_transaction_receipt_data.json"]
