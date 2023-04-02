from sqlalchemy import Column, ForeignKey, Identity, Integer, String, Table, list

from . import metadata

IssuingTransactionPurchaseDetailsJson = Table(
    "issuing_transaction_purchase_detailsjson",
    metadata,
    Column(
        "flight",
        IssuingTransactionFlightData,
        ForeignKey("IssuingTransactionFlightData"),
        comment="Information about the flight that was purchased with this transaction",
        nullable=True,
    ),
    Column(
        "fuel",
        IssuingTransactionFuelData,
        ForeignKey("IssuingTransactionFuelData"),
        comment="Information about fuel that was purchased with this transaction",
        nullable=True,
    ),
    Column(
        "lodging",
        IssuingTransactionLodgingData,
        ForeignKey("IssuingTransactionLodgingData"),
        comment="Information about lodging that was purchased with this transaction",
        nullable=True,
    ),
    Column("receipt", list, comment="The line items in the purchase", nullable=True),
    Column(
        "reference", String, comment="A merchant-specific order number", nullable=True
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["issuing_transaction_purchase_details.json"]
