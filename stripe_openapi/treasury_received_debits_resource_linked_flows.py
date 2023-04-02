from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

TreasuryReceivedDebitsResourceLinkedFlowsJson = Table(
    "treasury_received_debits_resource_linked_flowsjson",
    metadata,
    Column(
        "debit_reversal",
        String,
        comment="The DebitReversal created as a result of this ReceivedDebit being reversed",
        nullable=True,
    ),
    Column(
        "inbound_transfer",
        String,
        comment="Set if the ReceivedDebit is associated with an InboundTransfer's return of funds",
        nullable=True,
    ),
    Column(
        "issuing_authorization",
        String,
        comment="Set if the ReceivedDebit was created due to an [Issuing Authorization](https://stripe.com/docs/api#issuing_authorizations) object",
        nullable=True,
    ),
    Column(
        "issuing_transaction",
        String,
        comment="Set if the ReceivedDebit is also viewable as an [Issuing Dispute](https://stripe.com/docs/api#issuing_disputes) object",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["treasury_received_debits_resource_linked_flows.json"]
