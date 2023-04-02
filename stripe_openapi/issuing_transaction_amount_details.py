from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

IssuingTransactionAmountDetailsJson = Table(
    "issuing_transaction_amount_detailsjson",
    metadata,
    Column(
        "atm_fee",
        Integer,
        comment="The fee charged by the ATM for the cash withdrawal",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["issuing_transaction_amount_details.json"]
