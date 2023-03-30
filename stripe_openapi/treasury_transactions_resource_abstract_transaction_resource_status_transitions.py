from sqlalchemy import Column, Integer, Table

from . import metadata

TreasuryTransactionsResourceAbstractTransactionResourceStatusTransitions.Json = Table(
    "treasury_transactions_resource_abstract_transaction_resource_status_transitions.json",
    metadata,
    Column(
        "posted_at",
        Integer,
        comment="Timestamp describing when the Transaction changed status to `posted`",
        nullable=True,
    ),
    Column(
        "void_at",
        Integer,
        comment="Timestamp describing when the Transaction changed status to `void`",
        nullable=True,
        primary_key=True,
    ),
)
__all__ = [
    "treasury_transactions_resource_abstract_transaction_resource_status_transitions.json"
]
