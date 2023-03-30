from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

TreasuryReceivedDebitsResourceDebitReversalLinkedFlows.Json = Table(
    "treasury_received_debits_resource_debit_reversal_linked_flows.json",
    metadata,
    Column(
        "issuing_dispute",
        String,
        comment="Set if there is an Issuing dispute associated with the DebitReversal",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["treasury_received_debits_resource_debit_reversal_linked_flows.json"]
